pipeline {
    agent any
    stages {
        stage('build env') {
            options{
                timeout(time: 1, unit: 'HOURS')
                }
            steps {
                sh 'docker network create grid'
                sh 'docker-compose -f docker-compose.yml up -d'
            }
        }
        stage('run tests') {
            steps {
                sh 'docker exec -ti pytest python-cont --remote=True --hub=selenium-hub --browser=ff'
			}
		}
    }
        post {
            always {
                sh 'docker network rm grid'
                }
            }
}