pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'abhi/hitop'
    }

    stages {
        stage('Initialize') {
            steps {
                echo 'Initializing...'
            }
        }

        stage('Checkout Code') {
            steps {
                echo 'Checking out code...'
                git 'https://github.com/whoami-anoint/Hitop.git'
            }
        }

        stage('Unit Tests') {
            steps {
                echo 'Running unit tests...'
                sh 'pytest'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the project...'
                sh 'python build.py'
            }
        }

        stage('Static Code Analysis') {
            steps {
                echo 'Running static code analysis...'
                sh 'flake8 .'
            }
        }

        stage('Integration Tests') {
            steps {
                echo 'Running integration tests...'
                sh 'python integration_tests.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                script {
                    sh 'docker build -t $DOCKER_IMAGE_NAME .'
                }
            }
        }

        stage('Deploy to Staging') {
            steps {
                echo 'Deploying to staging environment...'
                sh 'kubectl apply -f staging.yaml'
            }
        }

        stage('Smoke Tests') {
            steps {
                echo 'Running smoke tests...'
                sh 'python smoke_tests.py'
            }
        }

        stage('Deploy to Production') {
            steps {
                echo 'Deploying to production environment...'
                sh 'kubectl apply -f production.yaml'
            }
        }

        stage('Cleanup') {
            steps {
                echo 'Cleaning up...'
                sh 'docker system prune -af'
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
