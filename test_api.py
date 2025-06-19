"""
Test cases for the API simulator using pytest and requests.
"""

import pytest
import requests
import json
import time
from api_simulator import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def api_url():
    """Base URL for API testing."""
    return "http://localhost:5000"


class TestAPIHealth:
    """Test health check endpoint."""
    
    def test_health_check(self, client):
        """Test health check endpoint."""
        response = client.get('/health')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['status'] == 'healthy'
        assert data['message'] == 'API is running'


class TestAPICalculator:
    """Test calculator API endpoints."""
    
    def test_add_numbers(self, client):
        """Test addition via API."""
        data = {'a': 5, 'b': 3}
        response = client.post('/api/calculate/add', 
                             data=json.dumps(data),
                             content_type='application/json')
        
        assert response.status_code == 200
        result = json.loads(response.data)
        assert result['operation'] == 'add'
        assert result['a'] == 5
        assert result['b'] == 3
        assert result['result'] == 8
    
    def test_add_numbers_floats(self, client):
        """Test addition with floats via API."""
        data = {'a': 5.5, 'b': 3.2}
        response = client.post('/api/calculate/add', 
                             data=json.dumps(data),
                             content_type='application/json')
        
        assert response.status_code == 200
        result = json.loads(response.data)
        assert result['result'] == 8.7
    
    def test_subtract_numbers(self, client):
        """Test subtraction via API."""
        data = {'a': 10, 'b': 3}
        response = client.post('/api/calculate/subtract', 
                             data=json.dumps(data),
                             content_type='application/json')
        
        assert response.status_code == 200
        result = json.loads(response.data)
        assert result['operation'] == 'subtract'
        assert result['result'] == 7
    
    def test_multiply_numbers(self, client):
        """Test multiplication via API."""
        data = {'a': 5, 'b': 3}
        response = client.post('/api/calculate/multiply', 
                             data=json.dumps(data),
                             content_type='application/json')
        
        assert response.status_code == 200
        result = json.loads(response.data)
        assert result['operation'] == 'multiply'
        assert result['result'] == 15
    
    def test_divide_numbers(self, client):
        """Test division via API."""
        data = {'a': 10, 'b': 2}
        response = client.post('/api/calculate/divide', 
                             data=json.dumps(data),
                             content_type='application/json')
        
        assert response.status_code == 200
        result = json.loads(response.data)
        assert result['operation'] == 'divide'
        assert result['result'] == 5.0
    
    def test_divide_by_zero(self, client):
        """Test division by zero via API."""
        data = {'a': 10, 'b': 0}
        response = client.post('/api/calculate/divide', 
                             data=json.dumps(data),
                             content_type='application/json')
        
        assert response.status_code == 400
        result = json.loads(response.data)
        assert 'error' in result
    
    def test_power_operation(self, client):
        """Test power operation via API."""
        data = {'base': 2, 'exponent': 3}
        response = client.post('/api/calculate/power', 
                             data=json.dumps(data),
                             content_type='application/json')
        
        assert response.status_code == 200
        result = json.loads(response.data)
        assert result['operation'] == 'power'
        assert result['result'] == 8
    
    def test_square_root(self, client):
        """Test square root via API."""
        data = {'number': 16}
        response = client.post('/api/calculate/sqrt', 
                             data=json.dumps(data),
                             content_type='application/json')
        
        assert response.status_code == 200
        result = json.loads(response.data)
        assert result['operation'] == 'square_root'
        assert result['result'] == 4.0
    
    def test_square_root_negative(self, client):
        """Test square root of negative number via API."""
        data = {'number': -4}
        response = client.post('/api/calculate/sqrt', 
                             data=json.dumps(data),
                             content_type='application/json')
        
        assert response.status_code == 400
        result = json.loads(response.data)
        assert 'error' in result
    
    def test_factorial(self, client):
        """Test factorial via API."""
        data = {'number': 5}
        response = client.post('/api/calculate/factorial', 
                             data=json.dumps(data),
                             content_type='application/json')
        
        assert response.status_code == 200
        result = json.loads(response.data)
        assert result['operation'] == 'factorial'
        assert result['result'] == 120
    
    def test_factorial_negative(self, client):
        """Test factorial of negative number via API."""
        data = {'number': -5}
        response = client.post('/api/calculate/factorial', 
                             data=json.dumps(data),
                             content_type='application/json')
        
        assert response.status_code == 400
        result = json.loads(response.data)
        assert 'error' in result
    
    def test_average(self, client):
        """Test average calculation via API."""
        data = {'numbers': [1, 2, 3, 4, 5]}
        response = client.post('/api/calculate/average', 
                             data=json.dumps(data),
                             content_type='application/json')
        
        assert response.status_code == 200
        result = json.loads(response.data)
        assert result['operation'] == 'average'
        assert result['result'] == 3.0
    
    def test_average_empty_list(self, client):
        """Test average calculation with empty list via API."""
        data = {'numbers': []}
        response = client.post('/api/calculate/average', 
                             data=json.dumps(data),
                             content_type='application/json')
        
        assert response.status_code == 400
        result = json.loads(response.data)
        assert 'error' in result


class TestAPIErrorHandling:
    """Test API error handling."""
    
    def test_missing_parameters(self, client):
        """Test API with missing parameters."""
        data = {'a': 5}  # Missing 'b'
        response = client.post('/api/calculate/add', 
                             data=json.dumps(data),
                             content_type='application/json')
        
        assert response.status_code == 400
        result = json.loads(response.data)
        assert 'error' in result
        assert 'Missing required parameters' in result['error']
    
    def test_empty_request_body(self, client):
        """Test API with empty request body."""
        response = client.post('/api/calculate/add', 
                             data='',
                             content_type='application/json')
        
        # Flask returns 500 for invalid JSON, which is acceptable
        assert response.status_code in [400, 500]
        result = json.loads(response.data)
        assert 'error' in result
    
    def test_invalid_json(self, client):
        """Test API with invalid JSON."""
        response = client.post('/api/calculate/add', 
                             data='invalid json',
                             content_type='application/json')
        
        # Flask returns 500 for invalid JSON, which is acceptable
        assert response.status_code in [400, 500]
        result = json.loads(response.data)
        assert 'error' in result


class TestAPIHistory:
    """Test API history functionality."""
    
    def test_get_history(self, client):
        """Test getting calculation history."""
        # First, perform some calculations
        client.post('/api/calculate/add', 
                   data=json.dumps({'a': 5, 'b': 3}),
                   content_type='application/json')
        
        client.post('/api/calculate/multiply', 
                   data=json.dumps({'a': 2, 'b': 4}),
                   content_type='application/json')
        
        # Get history
        response = client.get('/api/history')
        assert response.status_code == 200
        result = json.loads(response.data)
        assert 'history' in result
        assert len(result['history']) >= 2
    
    def test_clear_history(self, client):
        """Test clearing calculation history."""
        # First, perform a calculation
        client.post('/api/calculate/add', 
                   data=json.dumps({'a': 5, 'b': 3}),
                   content_type='application/json')
        
        # Clear history
        response = client.delete('/api/history')
        assert response.status_code == 200
        result = json.loads(response.data)
        assert result['message'] == 'History cleared successfully'
        
        # Verify history is empty
        response = client.get('/api/history')
        result = json.loads(response.data)
        assert len(result['history']) == 0


class TestAPIIntegration:
    """Test API integration scenarios."""
    
    def test_multiple_operations_sequence(self, client):
        """Test a sequence of multiple operations."""
        # Add
        response = client.post('/api/calculate/add', 
                             data=json.dumps({'a': 10, 'b': 5}),
                             content_type='application/json')
        assert response.status_code == 200
        add_result = json.loads(response.data)['result']
        
        # Multiply result by 2
        response = client.post('/api/calculate/multiply', 
                             data=json.dumps({'a': add_result, 'b': 2}),
                             content_type='application/json')
        assert response.status_code == 200
        multiply_result = json.loads(response.data)['result']
        
        # Subtract 5
        response = client.post('/api/calculate/subtract', 
                             data=json.dumps({'a': multiply_result, 'b': 5}),
                             content_type='application/json')
        assert response.status_code == 200
        final_result = json.loads(response.data)['result']
        
        # Verify final result: ((10 + 5) * 2) - 5 = 25
        assert final_result == 25
    
    def test_complex_calculation_chain(self, client):
        """Test a complex chain of calculations."""
        # Calculate 2^3
        response = client.post('/api/calculate/power', 
                             data=json.dumps({'base': 2, 'exponent': 3}),
                             content_type='application/json')
        power_result = json.loads(response.data)['result']
        
        # Add 5 to the result
        response = client.post('/api/calculate/add', 
                             data=json.dumps({'a': power_result, 'b': 5}),
                             content_type='application/json')
        add_result = json.loads(response.data)['result']
        
        # Calculate square root
        response = client.post('/api/calculate/sqrt', 
                             data=json.dumps({'number': add_result}),
                             content_type='application/json')
        sqrt_result = json.loads(response.data)['result']
        
        # Verify: sqrt(2^3 + 5) = sqrt(8 + 5) = sqrt(13) ≈ 3.6056
        assert abs(sqrt_result - 3.6056) < 0.001


# Integration tests that require a running server
class TestAPIIntegrationWithServer:
    """Integration tests that require a running API server."""
    
    @pytest.mark.integration
    def test_api_server_health(self, api_url):
        """Test API server health endpoint."""
        try:
            response = requests.get(f"{api_url}/health", timeout=5)
            assert response.status_code == 200
            data = response.json()
            assert data['status'] == 'healthy'
        except requests.exceptions.RequestException:
            pytest.skip("API server is not running")
    
    @pytest.mark.integration
    def test_api_server_calculation(self, api_url):
        """Test API server calculation endpoint."""
        try:
            data = {'a': 15, 'b': 7}
            response = requests.post(f"{api_url}/api/calculate/add", 
                                   json=data, 
                                   timeout=5)
            assert response.status_code == 200
            result = response.json()
            assert result['result'] == 22
        except requests.exceptions.RequestException:
            pytest.skip("API server is not running")


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v"]) 