#!/usr/bin/env python3
"""
Test runner script for local development.
"""

import subprocess
import sys
import os
import argparse


def run_command(command, description):
    """Run a command and handle errors."""
    print(f"\n{'='*50}")
    print(f"Running: {description}")
    print(f"Command: {command}")
    print('='*50)
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print("SUCCESS")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print("FAILED")
        print(f"Error: {e}")
        if e.stdout:
            print("STDOUT:", e.stdout)
        if e.stderr:
            print("STDERR:", e.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(description='Run tests for the calculator project')
    parser.add_argument('--unit', action='store_true', help='Run unit tests only')
    parser.add_argument('--api', action='store_true', help='Run API tests only')
    parser.add_argument('--integration', action='store_true', help='Run integration tests only')
    parser.add_argument('--coverage', action='store_true', help='Generate coverage report')
    parser.add_argument('--all', action='store_true', help='Run all tests with coverage')
    parser.add_argument('--server', action='store_true', help='Start the API server')
    
    args = parser.parse_args()
    
    # Check if virtual environment exists
    if not os.path.exists('venv'):
        print("Creating virtual environment...")
        if not run_command('python3 -m venv venv', 'Creating virtual environment'):
            sys.exit(1)
    
    # Install dependencies
    if not run_command('source venv/bin/activate && pip install -r requirements.txt', 'Installing dependencies'):
        sys.exit(1)
    
    if args.server:
        print("\nStarting API server...")
        print("Server will be available at http://localhost:5000")
        print("Press Ctrl+C to stop the server")
        try:
            subprocess.run('source venv/bin/activate && python api_simulator.py', shell=True)
        except KeyboardInterrupt:
            print("\nServer stopped.")
        return
    
    if args.unit:
        run_command('source venv/bin/activate && python -m pytest test_calculator.py -v', 'Unit Tests')
    
    elif args.api:
        run_command('source venv/bin/activate && python -m pytest test_api.py -v -m "not integration"', 'API Tests')
    
    elif args.integration:
        run_command('source venv/bin/activate && python -m pytest test_api.py -m integration -v', 'Integration Tests')
    
    elif args.coverage:
        run_command('source venv/bin/activate && python -m pytest --cov=calculator --cov=api_simulator --cov-report=html:htmlcov --cov-report=term-missing -m "not integration"', 'Coverage Report')
    
    elif args.all:
        print("Running all tests with coverage...")
        
        # Run unit tests
        if not run_command('source venv/bin/activate && python -m pytest test_calculator.py -v', 'Unit Tests'):
            print("Unit tests failed!")
            sys.exit(1)
        
        # Run API tests (excluding integration tests)
        if not run_command('source venv/bin/activate && python -m pytest test_api.py -v -m "not integration"', 'API Tests'):
            print("API tests failed!")
            sys.exit(1)
        
        # Generate coverage report
        if not run_command('source venv/bin/activate && python -m pytest --cov=calculator --cov=api_simulator --cov-report=html:htmlcov --cov-report=term-missing -m "not integration"', 'Coverage Report'):
            print("Coverage report generation failed!")
            sys.exit(1)
        
        print("\n🎉 All tests passed! Coverage report generated in htmlcov/")
    
    else:
        # Default: run all tests without coverage (excluding integration tests)
        print("Running all tests...")
        
        if not run_command('source venv/bin/activate && python -m pytest test_calculator.py test_api.py -v -m "not integration"', 'All Tests'):
            print("Tests failed!")
            sys.exit(1)
        
        print("\n🎉 All tests passed!")


if __name__ == '__main__':
    main() 