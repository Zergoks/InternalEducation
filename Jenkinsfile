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
                sh 'docker exec python-cont pytest -n 3 -m test --remote=True --hub=selenium-hub --browser=ff &'
                sh 'docker exec python-cont pytest -n 3 -m test --remote=True --hub=selenium-hub --browser=edge'
			}
		}
    }
        post {
            always {
                sh 'docker network rm grid'
                sh 'docker-compose down --remove-orphans'
                }
            }
}