# Automated Testing Pipeline with Python, pytest, and Jenkins

This project demonstrates a complete automated testing pipeline using Python, pytest, and Jenkins. It includes a calculator module, a REST API simulator, comprehensive test cases, and automated CI/CD pipeline configuration.

## 🚀 Features

- **Calculator Module**: Basic arithmetic operations and advanced mathematical functions
- **REST API Simulator**: Flask-based API with calculator endpoints
- **Comprehensive Testing**: Unit tests, API tests, and integration tests using pytest
- **Automated CI/CD**: Jenkins pipeline for continuous integration
- **Code Coverage**: Automated coverage reporting
- **Code Quality**: Linting and style checking

## 📁 Project Structure

```
automated-testing-pipeline-python-jenkins/
├── calculator.py          # Calculator module with mathematical operations
├── api_simulator.py       # Flask REST API simulator
├── test_calculator.py     # Unit tests for calculator module
├── test_api.py           # API tests and integration tests
├── requirements.txt      # Python dependencies
├── pytest.ini           # pytest configuration
├── Jenkinsfile          # Jenkins pipeline configuration
├── run_tests.py         # Local test runner script
└── README.md            # This file
```

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Git

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd automated-testing-pipeline-python-jenkins
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run tests**
   ```bash
   # Run all tests
   python -m pytest
   
   # Run with coverage
   python -m pytest --cov=calculator --cov=api_simulator --cov-report=html
   
   # Run specific test files
   python -m pytest test_calculator.py -v
   python -m pytest test_api.py -v
   ```

### Using the Test Runner Script

The project includes a convenient test runner script:

```bash
# Make the script executable
chmod +x run_tests.py

# Run all tests
./run_tests.py

# Run specific test types
./run_tests.py --unit      # Unit tests only
./run_tests.py --api       # API tests only
./run_tests.py --all       # All tests with coverage
./run_tests.py --server    # Start the API server
```

## 🧮 Calculator Module Usage

### Basic Operations

```python
from calculator import Calculator

calc = Calculator()

# Basic arithmetic
result = calc.add(5, 3)        # 8
result = calc.subtract(10, 4)   # 6
result = calc.multiply(3, 7)    # 21
result = calc.divide(15, 3)     # 5.0

# Advanced operations
result = calc.power(2, 3)       # 8
result = calc.square_root(16)   # 4.0
result = calc.factorial(5)      # 120
result = calc.average([1, 2, 3, 4, 5])  # 3.0

# History functionality
history = calc.get_history()
calc.clear_history()
```

### Standalone Functions

```python
from calculator import add, subtract, multiply, divide

result = add(5, 3)      # 8
result = subtract(10, 4) # 6
result = multiply(3, 7)  # 21
result = divide(15, 3)   # 5.0
```

## 🌐 API Usage

### Starting the API Server

```bash
python api_simulator.py
```

The server will start on `http://localhost:5000`

### API Endpoints

#### Health Check
```bash
GET /health
```

#### Calculator Operations
```bash
# Addition
POST /api/calculate/add
{
    "a": 5,
    "b": 3
}

# Subtraction
POST /api/calculate/subtract
{
    "a": 10,
    "b": 3
}

# Multiplication
POST /api/calculate/multiply
{
    "a": 5,
    "b": 3
}

# Division
POST /api/calculate/divide
{
    "a": 10,
    "b": 2
}

# Power
POST /api/calculate/power
{
    "base": 2,
    "exponent": 3
}

# Square Root
POST /api/calculate/sqrt
{
    "number": 16
}

# Factorial
POST /api/calculate/factorial
{
    "number": 5
}

# Average
POST /api/calculate/average
{
    "numbers": [1, 2, 3, 4, 5]
}
```

#### History Management
```bash
# Get calculation history
GET /api/history

# Clear calculation history
DELETE /api/history
```

### Example API Usage with curl

```bash
# Health check
curl http://localhost:5000/health

# Add two numbers
curl -X POST http://localhost:5000/api/calculate/add \
  -H "Content-Type: application/json" \
  -d '{"a": 5, "b": 3}'

# Get calculation history
curl http://localhost:5000/api/history
```

## 🧪 Testing

### Test Categories

1. **Unit Tests** (`test_calculator.py`)
   - Basic arithmetic operations
   - Advanced mathematical functions
   - Edge cases and error conditions
   - History functionality

2. **API Tests** (`test_api.py`)
   - API endpoint testing
   - Request/response validation
   - Error handling
   - Integration scenarios

3. **Integration Tests**
   - End-to-end API testing
   - Server communication tests

### Running Tests

```bash
# Run all tests
python -m pytest

# Run with verbose output
python -m pytest -v

# Run specific test file
python -m pytest test_calculator.py -v

# Run tests with coverage
python -m pytest --cov=calculator --cov=api_simulator --cov-report=html

# Run only integration tests
python -m pytest -m integration

# Run tests and generate JUnit XML reports
python -m pytest --junitxml=test-results.xml
```

### Test Coverage

The project includes comprehensive test coverage for:
- All calculator functions
- API endpoints
- Error handling
- Edge cases
- Integration scenarios

## 🔄 CI/CD Pipeline

### Jenkins Pipeline Features

The `Jenkinsfile` configures a complete CI/CD pipeline with:

1. **Environment Setup**
   - Python environment configuration
   - Virtual environment creation
   - Dependency installation

2. **Testing Stages**
   - Unit test execution
   - API test execution
   - Integration test execution

3. **Quality Assurance**
   - Code coverage reporting
   - Code quality checks (flake8, pylint)
   - Test result publishing

4. **Artifacts**
   - Test result archives
   - Coverage reports
   - HTML coverage reports

### Jenkins Setup

1. **Install Jenkins Plugins**
   - Pipeline
   - Git
   - JUnit
   - Cobertura
   - HTML Publisher

2. **Create Pipeline Job**
   - Create a new Pipeline job in Jenkins
   - Configure Git repository
   - Set the pipeline script from SCM
   - Point to the `Jenkinsfile`

3. **Configure Webhooks** (Optional)
   - Set up GitHub webhook to trigger builds on push
   - Configure Jenkins to receive webhook notifications

### Pipeline Stages

1. **Checkout**: Clone the repository
2. **Setup Python Environment**: Install Python and dependencies
3. **Create Virtual Environment**: Set up isolated Python environment
4. **Run Unit Tests**: Execute calculator unit tests
5. **Run API Tests**: Execute API tests
6. **Generate Coverage Report**: Create coverage reports
7. **Code Quality Check**: Run linting and style checks
8. **Integration Tests**: Run end-to-end tests

## 📊 Monitoring and Reporting

### Test Results
- JUnit XML reports for test results
- Test result trends and history
- Failed test analysis

### Code Coverage
- HTML coverage reports
- Coverage trends over time
- Coverage thresholds and alerts

### Code Quality
- Style checking results
- Code complexity analysis
- Quality metrics tracking

## 🚀 Deployment

### Local Development
```bash
# Start the API server
python api_simulator.py

# Run tests
python -m pytest

# Generate coverage report
python -m pytest --cov=calculator --cov=api_simulator --cov-report=html
```

### Production Deployment
1. Set up Jenkins server
2. Configure the pipeline job
3. Set up webhook integration with GitHub
4. Monitor pipeline execution and results

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

For issues and questions:
1. Check the existing issues
2. Create a new issue with detailed description
3. Include test cases and error messages

## 🔗 Related Resources

- [pytest Documentation](https://docs.pytest.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Jenkins Pipeline Documentation](https://www.jenkins.io/doc/book/pipeline/)
- [Python Testing Best Practices](https://realpython.com/python-testing/) 