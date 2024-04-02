pipeline {
    agent any

    stages {
        stage('Validate Docker-Compose') {
            steps {
                sh 'docker-compose -f docker-compose.yml config'
            }
        }
    }
}