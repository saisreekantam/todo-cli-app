pipeline {
    agent any
    
    environment {
        
        DOCKER_HUB_USERNAME = 'saivenkat1507'
        DOCKER_IMAGE_NAME = 'todo-cli'
        ROLL_NUMBER = 'IMT2023501' 
        DOCKER_CREDENTIALS_ID = 'docker-hub-credentials'
        GIT_CREDENTIALS_ID = 'github-creds'
    }
    
    stages {
        stage('Pull Code from GitHub') {
            steps {
                echo '📥 Stage 1: Pulling code from GitHub...'
                checkout scm
                echo '✅ Code pulled successfully from GitHub'
            }
        }
        
        stage('Build Code') {
            steps {
                echo '🔨 Stage 2: Building the code...'
                sh '''
                    echo "Validating Python files..."
                    python3 --version
                    python3 -m py_compile todo.py
                    python3 -m py_compile test_todo.py
                    echo "✅ Build successful - All Python files are valid"
                '''
            }
        }
        
        stage('Test Code') {
            steps {
                echo '🧪 Stage 3: Running tests...'
                sh '''
                    echo "Running unit tests..."
                    python3 test_todo.py
                    
                    if [ $? -eq 0 ]; then
                        echo "✅ All tests passed successfully!"
                    else
                        echo "❌ Tests failed!"
                        exit 1
                    fi
                '''
            }
        }
        
        stage('Create Docker Image') {
            when {
                expression {
                    return currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                echo '🐳 Stage 4: Creating Docker image...'
                script {
                    sh '''
                        echo "Building Docker image..."
                        docker build -t ${DOCKER_HUB_USERNAME}/${DOCKER_IMAGE_NAME}:latest \
                                     -t ${DOCKER_HUB_USERNAME}/${DOCKER_IMAGE_NAME}:${BUILD_NUMBER} \
                                     -f Dockerfile .
                        
                        echo "Listing Docker images..."
                        docker images | grep ${DOCKER_IMAGE_NAME}
                        
                        echo "✅ Docker image created successfully!"
                    '''
                }
            }
        }
        
        stage('Push to Docker Hub') {
            when {
                expression {
                    return currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                echo '📤 Stage 5: Pushing Docker image to Docker Hub...'
                script {
                    docker.withRegistry('https://registry.hub.docker.com', "${DOCKER_CREDENTIALS_ID}") {
                        sh '''
                            docker push ${DOCKER_HUB_USERNAME}/${DOCKER_IMAGE_NAME}:latest
                            docker push ${DOCKER_HUB_USERNAME}/${DOCKER_IMAGE_NAME}:${BUILD_NUMBER}
                            echo "✅ Docker image pushed to Docker Hub successfully!"
                        '''
                    }
                }
            }
        }
    }
    
    post {
        success {
            echo ''
            echo '✅ =================================================='
            echo '✅         PIPELINE COMPLETED SUCCESSFULLY!'
            echo '✅ =================================================='
            echo '✅  Application: To-Do List CLI'
            echo '✅  Build Number: ${BUILD_NUMBER}'
            echo '✅  Docker Image: ${DOCKER_HUB_USERNAME}/${DOCKER_IMAGE_NAME}:latest'
            echo '✅  Roll Number: ${ROLL_NUMBER}'
            echo '✅ =================================================='
            echo ''
            echo 'Docker Hub: https://hub.docker.com/r/${DOCKER_HUB_USERNAME}/${DOCKER_IMAGE_NAME}'
            echo ''
            echo 'To pull and run:'
            echo 'docker pull ${DOCKER_HUB_USERNAME}/${DOCKER_IMAGE_NAME}:latest'
            echo 'docker run -it ${DOCKER_HUB_USERNAME}/${DOCKER_IMAGE_NAME}:latest'
            echo ''
        }
        failure {
            echo ''
            echo '❌ =================================================='
            echo '❌              PIPELINE FAILED!'
            echo '❌ =================================================='
            echo '❌  Check console output for details'
            echo '❌  Build Number: ${BUILD_NUMBER}'
            echo '❌ =================================================='
            echo ''
        }
        always {
            echo '📊 Pipeline execution completed'
        }
    }
}