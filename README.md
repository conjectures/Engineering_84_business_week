# CICD

CICD, or **Continuous Integration**, **Continuous Delivery** and **Continuous Deployment** are the combined principles for automation in **building**, **testing** and **deployment** of applications.

### Continuous Integration
**Continuous Integration** is the practice of automatically merging changes to the main build branch often, with small increments. These changes are validated with tests designed to avoid integration challenges when merging.
The testing process should be automated, so that the merges can be performed quickly, without human intervention, while avoiding the situation where an integration breaks the main branch.

### Continuous Delivery
**Continuous Delivery** includes *Continuous Integration* but also merges the changes to a testing and/or production environmetn. That is, after a change is commited, it is automatically tested, pushed to the build stage, and the test/production environments, awaiting for deployment.

### Continuous Deployment
**Continuous Deployment** goes a step further and automates the deployment process.
Therefore, by practicing *Continuous Deployment*, we can have changes deployed and available to the end user faster and more frequently. 
This is due to the automated deployment operation; there should be no human intervention between the developer commiting the changes and the end user receiving the update, unless an error in validation occurs.

## Tools
- Jenkins
- Azure Pipelines
- Travis CI
- Gitlab CI
- Circle CI
- CodeShip
- TeamCity
