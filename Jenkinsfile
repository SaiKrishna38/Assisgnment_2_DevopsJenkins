pipeline{
    agent{
        docker{
            image 'python:3.9'
        }
    }
    stages{
        stage('checkout'){
            steps{
            git branch: 'main','https://github.com/SaiKrishna38/Devops_jenkins.git'
            }
        }
        stage('Install Dependencies'){
            steps{
                sh 'pip install --upfrade pip'
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