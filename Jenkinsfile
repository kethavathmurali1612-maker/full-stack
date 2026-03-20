pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/kethavathmurali1612-maker/full-stack.git'
            }
        }

        stage('Build Frontend Image') {
            steps {
                sh 'docker build -t kethavathmurali/2023bcd0008_frontend ./frontend'
            }
        }

        stage('Build Backend Image') {
            steps {
                sh 'docker build -t kethavathmurali/2023bcd0008_backend ./backend'
            }
        }

        stage('Push to DockerHub') {
            steps {
                sh 'docker push kethavathmurali/2023bcd0008_frontend'
                sh 'docker push kethavathmurali/2023bcd0008_backend'
            }
        }
    }
}
