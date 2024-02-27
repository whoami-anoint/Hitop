pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Checkout your repository
                git 'https://github.com/whoami-anoint/Hitop.git'
            }
        }
        
        stage('Run Flask App') {
            steps {
                // Change to the directory of your Flask app
                dir('Hitop') {
                    // Install dependencies
                    sh 'pip install -r requirements.txt'
                    
                    // Run Flask app
                    sh 'python app.py &'
                }
            }
        }
    }
}
