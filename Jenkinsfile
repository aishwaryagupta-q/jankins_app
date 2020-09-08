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
				sh "sudo apt get update"
				sh "sudo apt-get install python"
				sh "python --version"
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