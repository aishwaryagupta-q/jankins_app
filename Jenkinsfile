pipeline {
	agent any
	// tools {
	// 	// jdk 'name of installation in jenkins'
	// }
	parameters{
		// booleanParam(name: 'executeTests',defaultValue: true, description:"")
  		choice(  
            name: 'REQUESTED_ACTION',  
            choices: ['Build' , 'Test', "Deploy"],  
            description: '') 

	}
	environment{
		FLASK_APP= 'appl.py'
		// SERVER_CREDENTIALS = credentials('credentialID')
		//credential binding plugin
	}
	stages {
		stage("clean"){
			steps{
				deleteDir()
			}
		}
		stage('SCM'){
 			steps {
 				checkout scm
 				sh 'ls'
 				}
 			}
		stage("build"){

			steps{
				// sh "jenkins  ALL= NOPASSWD: ALL"
				sh "sudo apt-get update -y"
				sh  "sudo apt-get install python3-venv -y"
				sh	"python3 -m venv venv"
				sh	". venv/bin/activate"
				sh "pip3 install -r requirements.txt --user"
				// sh "sudo apt-get install -r requirements.txt"
				// sh "sudo easy_install pip"
				// sh "sudo apt-get install -y pylint"
				//  change
				// sh "export PATH=$HOME/.local/bin:$PATH"
				// sh "python3 --version"
				echo " BUILD stage completed Successfully"
		
			}
		}
		stage("test"){
			 when{  
                expression {params.REQUESTED_ACTION == 'Test' ||params.REQUESTED_ACTION == 'Deploy'}  
            }  
			steps{
				sh "pylint --rcfile google.cfg --reports=n --disable=deprecated-module appl.py || return 0 "
				sh "python3 -m unittest tests/test_routes.py"				
				echo " Test stage completed Successfully"
				// sh " shell script"
			}
		}
		stage("deploy"){
			when{
				expression {params.REQUESTED_ACTION == 'Deploy'}
			}
			steps{
				cleanWs()
				sh "sudo -i"
				sh "gcloud compute ssh --project training-freshers --zone us-central1-a aishwarya-jenkins-deployment"
				sh "git clone https://github.com/aishwaryagupta-q/jankins_app.git"
				sh script: '''
						#!/bin/bash
						ls -a
						cd ./jankins_app
						echo "this is $(pwd)"
						ls -a
						python3 -m venv venv
						. venv/bin/activate
						pip3 install -r requirements.txt --user
						pip3 install flask
						python3 appl.py &
						'''
				
				echo " Deploy stage completed Successfully"
			}
		}




	}
	post{  
        always{  
            // always executed  
            // cleanup  
            deleteDir()  
            cleanWs()  
            echo "All Executed"  
  
        }  
        success {  
            echo " Successfully"  
        }  
        failure {  
            echo " with failures in the pipeline"  
  
        }  
  
    }  
} 

