pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = '3.9'
        PIP_CACHE_DIR = '/tmp/pip-cache'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                script {
                    // Install Python if not available
                    sh '''
                        if ! command -v python3 &> /dev/null; then
                            echo "Python3 not found, installing..."
                            sudo apt-get update
                            sudo apt-get install -y python3 python3-pip python3-venv
                        fi
                        
                        python3 --version
                        pip3 --version
                    '''
                }
            }
        }
        
        stage('Create Virtual Environment') {
            steps {
                script {
                    sh '''
                        python3 -m venv venv
                        source venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }
        
        stage('Run Unit Tests') {
            steps {
                script {
                    sh '''
                        source venv/bin/activate
                        python -m pytest test_calculator.py -v --junitxml=test-results/unit-tests.xml
                    '''
                }
            }
            post {
                always {
                    publishTestResults testResultsPattern: 'test-results/*.xml'
                }
            }
        }
        
        stage('Run API Tests') {
            steps {
                script {
                    sh '''
                        source venv/bin/activate
                        python -m pytest test_api.py -v --junitxml=test-results/api-tests.xml
                    '''
                }
            }
            post {
                always {
                    publishTestResults testResultsPattern: 'test-results/*.xml'
                }
            }
        }
        
        stage('Generate Coverage Report') {
            steps {
                script {
                    sh '''
                        source venv/bin/activate
                        python -m pytest --cov=calculator --cov=api_simulator --cov-report=html:htmlcov --cov-report=xml:coverage.xml
                    '''
                }
            }
            post {
                always {
                    publishCoverage adapters: [coberturaAdapter('coverage.xml')], sourceFileResolver: sourceFiles('STORE_LAST_BUILD')
                    publishHTML([
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'htmlcov',
                        reportFiles: 'index.html',
                        reportName: 'Coverage Report'
                    ])
                }
            }
        }
        
        stage('Code Quality Check') {
            steps {
                script {
                    sh '''
                        source venv/bin/activate
                        # Install additional tools for code quality
                        pip install flake8 pylint
                        
                        # Run flake8 for style checking
                        flake8 calculator.py api_simulator.py --max-line-length=100 --count --statistics || true
                        
                        # Run pylint for code analysis
                        pylint calculator.py api_simulator.py --disable=C0114,C0116 || true
                    '''
                }
            }
        }
        
        stage('Integration Tests') {
            steps {
                script {
                    sh '''
                        source venv/bin/activate
                        
                        # Start the API server in background
                        python api_simulator.py &
                        API_PID=$!
                        
                        # Wait for server to start
                        sleep 5
                        
                        # Run integration tests
                        python -m pytest test_api.py -m integration -v --junitxml=test-results/integration-tests.xml || true
                        
                        # Stop the API server
                        kill $API_PID || true
                    '''
                }
            }
            post {
                always {
                    publishTestResults testResultsPattern: 'test-results/*.xml'
                }
            }
        }
    }
    
    post {
        always {
            script {
                // Clean up virtual environment
                sh 'rm -rf venv || true'
                
                // Archive test results
                archiveArtifacts artifacts: 'test-results/**/*', allowEmptyArchive: true
                archiveArtifacts artifacts: 'htmlcov/**/*', allowEmptyArchive: true
                archiveArtifacts artifacts: 'coverage.xml', allowEmptyArchive: true
            }
        }
        
        success {
            echo 'Pipeline completed successfully!'
        }
        
        failure {
            echo 'Pipeline failed!'
        }
        
        unstable {
            echo 'Pipeline is unstable!'
        }
    }
} 