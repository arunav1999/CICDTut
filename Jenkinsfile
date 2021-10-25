pipeline
{
	agent any
	stages
	{
		stage("Compile")
		{
			steps
			{
				//sh "/.python mainFile.py"
				echo "Source code is compliled"
			}
		}
		stage("Unit Test")
		{
			steps
			{
				sh "/. python3 unitTests.py"
			}
		}
	}
}