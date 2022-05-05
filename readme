This folder is a simple way to create, test and then deploy a Kubernetes cluster using CloudFormation.

The CloudFormation EKS Cluster Template is the amazon-eks-controlpane-template.yaml file.
The .pre-commit-config.yaml file is for running unit tests on the template before uploading the stack to AWS or including it in our CI/CD pipeline
To run the tests, you must ensure that python3.9 is installed
Then cd to the project folder on your terminal and run

pre-commit run --all-files

All the tests should run and show the green "passed"

The tests being run on the templates are Trim Trailing white space, End for file space, CFN-Lint and CFN-Nag. T
To further test, cloud radar can be used to perform python unit tests that will simulate the launching of the resources and verify that they are accurately launched.
