pipeline{
    agent{
        docker{
            image 'python:3.9'
            args '-u root'
        }
    }
    stages{
        stage('Install Dependencies'){
            steps{
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests'){
            steps{
                sh 'pytest test_calculator.py'
            }
        }
    }
    post{
        success{
            echo 'All tests passed successfully'
        }
        failure{
            echo 'Tests failed'
        }
    }
}
