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
            }
        }

        stage('Unit Tests') {
            steps {
                echo 'Running unit tests...'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the project...'
            }
        }

        stage('Static Code Analysis') {
            steps {
                echo 'Running static code analysis...'
            }
        }

        stage('Integration Tests') {
            steps {
                echo 'Running integration tests...'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image with Nginx
                    sh 'docker build -t $DOCKER_IMAGE_NAME .'
                }
            }
        }

        stage('Deploy to Staging') {
            steps {
                echo 'Deploying to staging environment...'
            }
        }

        stage('Smoke Tests') {
            steps {
                echo 'Running smoke tests...'
            }
        }

        stage('Deploy to Production') {
            steps {
                echo 'Deploying to production environment...'
            }
        }

        stage('Cleanup') {
            steps {
                echo 'Cleaning up...'
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
