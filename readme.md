# EKS Cloud Formation Template Linter

This project is a simple way to create, lint, and deploy a basic Kubernetes cluster using CloudFormation. However, the CloudFormation template included in the project can be replaced by any CloudFormation template and it would work.

## Problem Statement

CloudFormation templates usually throw all sorts of errors that might not be caught by traditional linters. Sometimes the errors are not caught until much later on after a lot of resources have already been deployed, which could lead to a lot of problems. This particular linter checks that the resources being deployed are deployed in the right order, checks the syntax, and ensures that no errors occur during deployment.

## File Structure

The following files are included in this project:

- `amazon-eks-controlplane-template.yaml`: This is the CloudFormation EKS Cluster Template. Ideally, this program works with any type of CloudFormation template.
- `.pre-commit-config.yaml`: This file is used for running unit tests on the template before uploading the stack to AWS or including it in our CI/CD pipeline.
- `requirements.txt`: This can be installed before running the file, but ideally, you only need Python 3.9 installed on the device that this program is run on.

## How to Run the Program

To run the tests, you must ensure that Python 3.9 is installed. Follow these steps:

1. Ensure you replace the `amazon-eks-controlpane-template.yaml` with the CloudFormation file you want to lint.
2. Replace the file name in `.pre-commit-config.yaml` with the CloudFormation file name to be linted.
3. `cd` to the project folder on your terminal.
4. Run `pre-commit run --all-files`.
5. All the tests should run and show the green "passed".

The tests being run on the templates are:

- Trim Trailing white space
- End for file space
- CFN-Lint
- CFN-Nag

## Future Improvements

To further extend this project, cloud radar can be used to perform Python unit tests that will simulate the launching of the resources and verify that they are accurately launched.
