pipeline {
    agent any

environment {
        APP_NAME = 'MyApp'
        APP_VERSION = '1.0.0'
        DOCKER_REPO = 'aviel770'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo "Stage name is: ${env.STAGE_NAME}"
                echo 'Building the project...'
                sh "echo 'No build steps configured yet' >> app.txt"
                echo "echo 'Application Name: ${APP_NAME}'"
                echo "echo 'Application Version: ${APP_VERSION}'"
                echo "echo 'Docker Repository: ${DOCKER_REPO}'"
            }
        }

        stage('Test') {
            steps {
                echo "Stage name is: ${env.STAGE_NAME}"
                echo 'Running tests...'
                echo "Pipeline name is: ${env.JOB_NAME}"
                echo "Build number is: ${env.BUILD_NUMBER}"
                echo "Pipeline name is: ${env.JOB_NAME}_${env.BUILD_NUMBER}"
                sh 'ls -la'
            }
        }
        stage('Deploy') {
            steps {
                echo "Stage name is: ${env.STAGE_NAME}"
                echo 'Deploying the application...'
                sh 'mkdir -p deploy && mv app.txt deploy/'
                sh 'ls -laR'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Build succeeded.'
        }
        failure {
            echo 'Build failed.'
        }
        cleanup {
            cleanWs()
        }
    }
}
