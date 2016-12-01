node {
    stage 'Prepare env'
    env.WORKSPACE = pwd()
    def home = "${env.WORKSPACE}"
    stage 'Checkout latest code from repository'
    checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/otgcjm/devopstest.git']]])
    try {
    stage 'build locust image'                      
    sh """
        docker build -t hry/locust docker/locust
        docker save -o /mnt/jenkins/tmp-images/locust.img hry/locust
        rm -rf /tmp/locust
        cp -r "${home}/docker/locust" /tmp
    """

    stage 'launch locust ec2 instances'
    sh """
        /usr/bin/ansible-playbook --private-key ~/.ssh/camtest.pem "${home}/ansible/locust-ec2.yaml"
    """
    stage "install locust"
    sh """
        /usr/bin/ansible-playbook --private-key ~/.ssh/camtest.pem "${home}/ansible/locust-inst.yaml"
    """    
    }
    catch (err) {
        throw err
    } finally {
        println("complete")
    }
}
