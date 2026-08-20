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
                sh 'ls -la'
            }
        }

        stage('Test') {
            steps {
                echo "Stage name is: ${env.STAGE_NAME}"
                echo 'Running tests...'
                sh 'echo "No tests configured yet"'
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
