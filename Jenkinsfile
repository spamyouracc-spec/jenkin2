pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Generate Report') {
            steps {
                echo "BUILD_NUMBER: ${env.BUILD_NUMBER}"
                echo "JOB_NAME: ${env.JOB_NAME}"
                echo "WORKSPACE: ${env.WORKSPACE}"

                bat 'python app.py'

                bat 'type build_report.txt'
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'build_report.txt',fingerprint : true
            }
        }
    }

    


