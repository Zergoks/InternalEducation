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
                sh 'docker exec python-cont pytest -n 3 -m test --reruns 5 --remote=True --hub=selenium-hub --browser=ff --alluredir=/usr/src/app/allure-report/'
                //sh 'docker exec python-cont pytest -m smoke --remote=True --hub=selenium-hub --browser=edge --alluredir=/allure-report'
			}
		}
    }
        post {
            always {
                allure ([
                            includeProperties: false,
                            jdk: '',
                            reportBuildPolicy: 'ALWAYS',
                            results: [[path: '/allure-report']]
                            ])
                sh 'docker network rm grid'
                sh 'docker-compose down --remove-orphans'
                }
            }
}