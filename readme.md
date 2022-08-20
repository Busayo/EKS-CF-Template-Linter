# Program that lints an EKS Cloud Formation Template

This project is a simple way to create, test and then deploy a basic Kubernetes cluster using CloudFormation. However, the Cloud Formation template can be replaced by any Cloud Formation template and it would work.


### File Structure

* amazon-eks-controlpane-template.yaml file: This is the CloudFormation EKS Cluster Template
* .pre-commit-config.yaml file: This is used for running unit tests on the template before uploading the stack to AWS or including it in our CI/CD pipeline
* requirements.txt: This can be installed before running the file but ideally you only need python3.9 installed on the device that this program is run on.


### How to run the program

* To run the tests, you must ensure that python3.9 is installed
* Then cd to the project folder on your terminal and run <pre-commit run --all-files>

All the tests should run and show the green "passed"

The tests being run on the templates are Trim Trailing white space, End for file space, CFN-Lint and CFN-Nag. 

### Future Improvements

To further extend this project, cloud radar can be used to perform python unit tests that will simulate the launching of the resources and verify that they are accurately launched.
