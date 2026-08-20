pipeline {
    agent any

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
            }
        }

        stage('Test') {
            steps {
                echo "Stage name is: ${env.STAGE_NAME}"
                echo 'Running tests...'
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
