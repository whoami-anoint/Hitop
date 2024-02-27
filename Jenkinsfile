pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git clone 'https://github.com/whoami-anoint/Hitop.git'
            }
        }
        
        stage('Run Flask App') {
            steps {
                dir('Hitop') {
                    sh 'python app.py &'
                }
            }
        }
    }
}
