pipeline {
    agent any

    environment {
        IMAGE_NAME = "smart-rental"
        IMAGE_TAG = "latest"
        CONTAINER_NAME = "smart-rental-container"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %IMAGE_NAME%:%IMAGE_TAG% ."
            }
        }

        stage('Stop Old Container (if running)') {
            steps {
                bat "docker stop %CONTAINER_NAME% || exit 0"
                bat "docker rm %CONTAINER_NAME% || exit 0"
            }
        }

        stage('Run Docker Container') {
            steps {
                bat "docker run -d -p 8000:8000 --name %CONTAINER_NAME% %IMAGE_NAME%:%IMAGE_TAG%"
            }
        }
    }

    post {
        success {
            echo 'Docker Build & Deployment Successful 🚀'
        }
        failure {
            echo 'Pipeline Failed ❌'
        }
    }
}