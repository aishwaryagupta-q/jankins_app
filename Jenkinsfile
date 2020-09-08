pipeline {
	agent any
	// tools {
	// 	// jdk 'name of installation in jenkins'
	// }
	parameters{
		booleanParam(name: 'executeTests',defaultValue: true, description:"")
	}
	environment{
		FLASK_APP= 'appl.py'
		// SERVER_CREDENTIALS = credentials('credentialID')
		//credential binding plugin
	}
	stages {
		stage("build"){
			when{
				expression {
					//env.BRANCH_NAME == 'dev' || 
					params.executeTests
					//if true then runs
				}
			}
			steps{
				// sh "jenkins  ALL= NOPASSWD: ALL"
				sh "sudo apt-get update -y"
				sh "sudo apt-get install python3 -y"
				// sh	"sudo apt-get install python3-pip -y"
				sh	"sudo apt-get install python3-venv -y"
				sh	"python3 -m venv venv"
				sh	"venv/bin/activate"
				sh "python3 --version"
				echo " running stage"
				// sh " shell script"
			}
		}


	}
	post{
		always{
			// always executed
			echo " always post"
			deleteDir()
		}
		success {
			echo "success post"
		}
		failure {
			echo "failure post"

		}

	}
}