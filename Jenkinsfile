pipeline {
    agent any

    stages {

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

               sh 'docker login -u kethavathmurali -p Mur@li12345'
                sh 'docker push kethavathmurali/2023bcd0008_frontend'
                sh 'docker push kethavathmurali/2023bcd0008_backend'
            }
        }
    }
}
