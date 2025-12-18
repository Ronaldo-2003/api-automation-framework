pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run API Tests') {
            steps {
                sh '. venv/bin/activate && pytest -v'
            }
        }
    }

    post {
        success {
            echo 'All API tests passed'
        }
        failure {
            echo 'API tests failed'
        }
    }
}
