pipeline {
    agent any 

    environment {
        // Define your DockerHub credentialsId, repo name, and tag name
        DOCKER_CREDENTIALS_ID = 'roseaw-dockerhub'
        DOCKER_IMAGE = 'cithit/roseaw-cyberrange'
        IMAGE_TAG = 'latest'
        GITHUB_URL = 'https://github.com/miamioh-roseaw/cyberrange.git'
        
        // Define your Kubernetes cluster credentials
        KUBECONFIG = credentials('roseaw-heavy-metal')
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the specified GitHub repository
                checkout([$class: 'GitSCM', branches: [[name: '*/main']],
                          userRemoteConfigs: [[url: "${GITHUB_URL}"]]])
            }
        }
        stage('Build Docker Image') {
            steps {
                // Build Docker Image
                script {
                    docker.build("${DOCKER_IMAGE}:${IMAGE_TAG}")
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    // Push Docker Image to DockerHub
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKER_CREDENTIALS_ID}") {
                        docker.image("${DOCKER_IMAGE}:${IMAGE_TAG}").push()
                    }
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    // Set up Kubernetes configuration using the specified KUBECONFIG
                    def kubeConfig = readFile(KUBECONFIG)
                    sh "kubectl --kubeconfig=\$KUBECONFIG apply -f deployment.yaml"
                    sh "kubectl get all -A"
                }
            }
        }
    }
}
