pipeline {
    agent any
    stages {
        stage('build selenium env') {
            options{
                timeout(time: 1, unit: 'HOURS')
                }
            steps {
                sh 'docker network create grid'
                sh 'docker-compose -f docker-compose.yml up -d'
            }
        }
        stage('build python') {
            options{
                timeout(time: 1, unit: 'HOURS')
                }
            steps {
                sh 'docker build -t python_test:latest .'
                sh 'docker run --name python-cont python_test:latest'
                sh 'docker exec -ti python-cont pip install --no-cache-dir -r requirements.txt'
            }
        }
        stage('run tests') {
            steps {
               // sh 'docker exec [OPTIONS] CONTAINER COMMAND [ARG...]'
                sh 'docker exec -ti pytest --remote=True --hub=localhost --browser=ff'
               // sh 'pytest --remote=True --hub=localhost --browser=ff'
			}
		}
    }
        post {
            always {
                sh 'docker network rm grid'
                sh 'docker rm python-cont'
                }
            }
}