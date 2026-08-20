pipeline {
    agent any

environment {
        APP_NAME = 'MyApp'
        APP_VERSION = '1.0.0'
        DOCKER_REPO = 'aviel770'
        FILE_TO_TEST = './build-info.txt'
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
                echo "'Application Name: ${APP_NAME}'"
                echo "'Application Version: ${APP_VERSION}'"
                echo "'Docker Repository: ${DOCKER_REPO}'"
                sh 'touch build-info.txt'
                echo "Application Name: ${APP_NAME}" >> build-info.txt
                echo "Build Number: ${env.BUILD_NUMBER}" >> build-info.txt
                echo "Build Timestamp: ${new Date().format('yyyy-MM-dd HH:mm:ss')}" >> build-info.txt
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
                stage('Check if app.txt exists') {
                    steps {
                        script {
                            if (fileExists(FILE_TO_TEST)) {
                                echo "File ${FILE_TO_TEST} exists."
                            } else {
                                error "File ${FILE_TO_TEST} does not exist."
                            }
                        }
                    }
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
            echo 'Pipeline finished.' (0)
        }
        success {
            echo 'Build succeeded.' (0)
        }
        failure {
            echo 'Build failed.' (1)
        }
        cleanup {
            cleanWs()
        }
    }
}
