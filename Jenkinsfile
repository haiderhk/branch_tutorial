pipeline {
    agent any

    stages {
        
        stage('Prepare .env') {
            steps {
                script {
                    sh 'cp .env.example .env'
                }
            }
        }    
        stage('Validate Docker-Compose') {
            steps {
                script {
                    // Running docker-compose config command within a docker-compose container
                    sh 'docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v "${PWD}":/work -w /work docker/compose:1.29.2 config'
                }
            }
        }
    }
}
