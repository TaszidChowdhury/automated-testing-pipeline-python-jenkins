"""
Simple REST API Simulator
A basic Flask API for demonstrating automated testing.
"""

from flask import Flask, request, jsonify
from calculator import Calculator
import json

app = Flask(__name__)
calculator = Calculator()

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'message': 'API is running'
    }), 200

@app.route('/api/calculate/add', methods=['POST'])
def add_numbers():
    """Add two numbers via API."""
    try:
        data = request.get_json()
        if not data or 'a' not in data or 'b' not in data:
            return jsonify({'error': 'Missing required parameters: a and b'}), 400
        
        a = float(data['a'])
        b = float(data['b'])
        result = calculator.add(a, b)
        
        return jsonify({
            'operation': 'add',
            'a': a,
            'b': b,
            'result': result
        }), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/calculate/subtract', methods=['POST'])
def subtract_numbers():
    """Subtract two numbers via API."""
    try:
        data = request.get_json()
        if not data or 'a' not in data or 'b' not in data:
            return jsonify({'error': 'Missing required parameters: a and b'}), 400
        
        a = float(data['a'])
        b = float(data['b'])
        result = calculator.subtract(a, b)
        
        return jsonify({
            'operation': 'subtract',
            'a': a,
            'b': b,
            'result': result
        }), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/calculate/multiply', methods=['POST'])
def multiply_numbers():
    """Multiply two numbers via API."""
    try:
        data = request.get_json()
        if not data or 'a' not in data or 'b' not in data:
            return jsonify({'error': 'Missing required parameters: a and b'}), 400
        
        a = float(data['a'])
        b = float(data['b'])
        result = calculator.multiply(a, b)
        
        return jsonify({
            'operation': 'multiply',
            'a': a,
            'b': b,
            'result': result
        }), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/calculate/divide', methods=['POST'])
def divide_numbers():
    """Divide two numbers via API."""
    try:
        data = request.get_json()
        if not data or 'a' not in data or 'b' not in data:
            return jsonify({'error': 'Missing required parameters: a and b'}), 400
        
        a = float(data['a'])
        b = float(data['b'])
        result = calculator.divide(a, b)
        
        return jsonify({
            'operation': 'divide',
            'a': a,
            'b': b,
            'result': result
        }), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/calculate/power', methods=['POST'])
def power_numbers():
    """Raise a number to a power via API."""
    try:
        data = request.get_json()
        if not data or 'base' not in data or 'exponent' not in data:
            return jsonify({'error': 'Missing required parameters: base and exponent'}), 400
        
        base = float(data['base'])
        exponent = float(data['exponent'])
        result = calculator.power(base, exponent)
        
        return jsonify({
            'operation': 'power',
            'base': base,
            'exponent': exponent,
            'result': result
        }), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/calculate/sqrt', methods=['POST'])
def square_root():
    """Calculate square root via API."""
    try:
        data = request.get_json()
        if not data or 'number' not in data:
            return jsonify({'error': 'Missing required parameter: number'}), 400
        
        number = float(data['number'])
        result = calculator.square_root(number)
        
        return jsonify({
            'operation': 'square_root',
            'number': number,
            'result': result
        }), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/calculate/factorial', methods=['POST'])
def factorial():
    """Calculate factorial via API."""
    try:
        data = request.get_json()
        if not data or 'number' not in data:
            return jsonify({'error': 'Missing required parameter: number'}), 400
        
        number = int(data['number'])
        result = calculator.factorial(number)
        
        return jsonify({
            'operation': 'factorial',
            'number': number,
            'result': result
        }), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/calculate/average', methods=['POST'])
def average():
    """Calculate average via API."""
    try:
        data = request.get_json()
        if not data or 'numbers' not in data:
            return jsonify({'error': 'Missing required parameter: numbers'}), 400
        
        numbers = [float(x) for x in data['numbers']]
        result = calculator.average(numbers)
        
        return jsonify({
            'operation': 'average',
            'numbers': numbers,
            'result': result
        }), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/history', methods=['GET'])
def get_history():
    """Get calculation history."""
    return jsonify({
        'history': calculator.get_history()
    }), 200

@app.route('/api/history', methods=['DELETE'])
def clear_history():
    """Clear calculation history."""
    calculator.clear_history()
    return jsonify({
        'message': 'History cleared successfully'
    }), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 