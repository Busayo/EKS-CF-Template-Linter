# Program that lints an EKS Cloud Formation Template

This project is a simple way to create, lint and then deploy a basic Kubernetes cluster using CloudFormation. However, the Cloud Formation template included in the project can be replaced by any Cloud Formation template and it would work.

### Problem statement

Cloud formation templates usually throw all sorts of errors that might not be caught by traditional linters. Sometimes the errrors are not caught till much later on after a lot of resources have already being deployed which could be lead to a lot of problems. This particular linter checks that the resources being deployed are deployed in the right order, checks the syntax and ensures that no errors occur during deployment.

### File Structure

* amazon-eks-controlpane-template.yaml file: This is the CloudFormation EKS Cluster Template. Ideally, this program works with any type of cloudformation template.
* .pre-commit-config.yaml file: This is used for running unit tests on the template before uploading the stack to AWS or including it in our CI/CD pipeline
* requirements.txt: This can be installed before running the file but ideally you only need python3.9 installed on the device that this program is run on.


### How to run the program

* To run the tests, you must ensure that python3.9 is installed.
* Ensure you replace the amazon-eks-controlpane-template.yaml with the CF file you want to lint, also replace the file name in .pre-commit-config.yaml with the CF file name to be linted.
* Then cd to the project folder on your terminal and run <pre-commit run --all-files>

All the tests should run and show the green "passed"

The tests being run on the templates are Trim Trailing white space, End for file space, CFN-Lint and CFN-Nag. 

### Future Improvements

To further extend this project, cloud radar can be used to perform python unit tests that will simulate the launching of the resources and verify that they are accurately launched.
