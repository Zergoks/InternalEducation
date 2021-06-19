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
                sh 'docker exec python-cont pytest -m test --remote=True --hub=selenium-hub --browser=ff --alluredir=/var/jenkins_home/allure-report &'
                sh 'docker exec python-cont pytest -m test --remote=True --hub=selenium-hub --browser=edge --alluredir=/var/jenkins_home/allure-report'
			}
		}
    }
        post {
            always {
                allure ([
                            includeProperties: false,
                            jdk: '',
                            reportBuildPolicy: 'ALWAYS',
                            results: [[path: '/var/jenkins_home/allure-report']]
                            ])
                sh 'docker network rm grid'
                sh 'docker-compose down --remove-orphans'
                }
            }
}