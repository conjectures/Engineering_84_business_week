# Cloud Computing

## Introduction

### What is Cloud Computing
Cloud computing is the practice of using and paying for servers and computing resources on demand, over the internet. The servers are set up and maintained by a third party, instead of having your own servers to host products.

### What are the benefits of cloud computing
The benefits of using cloud computing is, as opposed to using your own servers are:
- Cost Savings

  Using cloud computing may reduce the cost of managing and maintaining IT systems. Rather than purchasing expensive systems and equipment, most companies reduce costs by using the resources of cloud computing service providers. 
  As many businesses have seasonal traffic, or even may have most traffic on predictable hours of the day, they can make use of only of the resources they need, and therefore reduce costs when there is not a lot of demand.

- Scalability

  Businesses that use cloud computing can scale up or down their operation and storage according to their needs. 
  Rather than purchasing and installing expensive servers by themselves, they use the servers provided by the cloud computing and can in a moments notice, they can increase or decrease the number of servers, or their capabilities, to suit their needs.

- **Reliability**

  Well established cloud computing providers can boast of highly reliable servers with minimal down time, as their business model is reliant on this aspect.
  With the use of reproducability and automation tools, a different server can be spun up with the same state, in the small chance that our original server goes down.

- ***Security*

  Depending on the provider, many cloud services have firewalls and other protection methods against malicious attacks. Additionally, they can provide backups and other support for sensitive data.


### Cloud Computing types
- **Private Cloud**: Clouds hosted and maintained by the user.
- **Public Cloud**: Clouds that are hosted and maintained by a cloud computing provider
- **Hybrid Cloud**: A combination of the above two types

### Scaling
Scaling refers to changing the capabilities of the hosting servers with the goal of adapting the throughput of the application. As traffic increases or decreases, we need to scale up or scale down accordingly so that the application needs are met. There are two types of scaling that can be applied:

- **Horizontal Scaling**

Refers to the increase or decrease of the number of servers that are used. Typically, an 'image' or snapshot of a running server is made so that different replica sets can be made of the first one. 
Having many servers can increase the amount of users the application can serve, as the servers are working in parallel.

- **Vertical Scaling**

This type of scaling refers to 'upgrading' the server where the application is hosted so that it can serve users faster. Additionally, with a more capable server, more threads can be created that can also serve customers concurrently.

![Horizontal vs Vertical Scaling](horizontal-vertical-scaling-diagram.png)

## Architecture

# ## One tier architecture
# ## Two tier architecture
# ## Three tier architecture

# AWS

## What is AWS
AWS is the larger cloud computing provider with servers in every continent. AWS are trusted by large companies like Netflix, BBC, Facebook and Twitch, which accentuates their reliability and range of services.
The benefits of AWS over its competitors is that their services are efficient, competitive and reliable. 
Security group works in the instance level


## Getting started with AWS
To get started with AWS we need to either create new user, or acquire an IAM access role to work in an organisation's account.

## EC2 - Elastic Compute Cloud
Elastic Compute Cloud is an AWS service that provides secure, resizable compute capacity in the cloud. They are virtual machines hosted on the cloud, which means that we can choose an operating system, CPU capabilies, memory capacity and other settings, according to our needs.
EC2 instances are charged according to the time they spend on *Running* state, and have a mutliplier applied according to their CPU and RAM capabiliy 'level'. 

### Creating an EC2 Instance
To create an EC2 instance, we first need to go to the EC2 panel. From there we press the 'Create new Instance' button, and we are met with a number of settings we can choose:
1. Image

We first need to choose an AMI image for the EC2 instance. There are many 'blank' images that only include the operating system, but we can create our own AMI image in the future that includes custom installation of software we might need.

2. Provisioning

At this stage, we need to choose the capabilites of the instance. There is a free tier available for free 


Image
CPU Tier
Settings
Storage
Tags
Security Groups
ss

## Connecting to Instance

## Copying files
We can copy files to our newly created EC2 instance with the `scp` command

