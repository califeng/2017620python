pipeline {
  agent {
    node {
      label 'k8snode1'
    }

  }
  stages {
    stage('1') {
      steps {
        sh 'echo  "hello,world"'
      }
    }

  }
  environment {
    author = 'feng'
  }
}