
# AWS Guide
In this guide, we show how to create AWS resources with the online console provided by Amazon.

## Table of Contents
- [VPC](#vpc)
- [Subnets](#subnets)
- [Internet Gateway](#internet-gateway)
- [Network ACL](#network-acl)
- [Security Groups](#security-groups)
- [EC2](#ec2)
- [Scenario](#scenario)

## VPC
To create a *Virtual Private Cloud*, we first need to find the VPC option on the services panel. We can search for it on any page with the `Alt+S` keyboard shortcut.
We then need to go to the "*Your VPCs*" tab found on the left side pane. After pressing the option, we are greeted with a list of all the existing VPCs in the current *Region*.
If no VPCs have been made yet, only the default VPC can be seen here. 

![VPC list](media/create_vpc.png)

From this page, choose the orange button on the upper-right side of the page, labeled '*Create VPC'.
Then, we are presented with a page where we can fill the settings for our new VPC:

![VPC details](media/vpc_details.png)

The name of the VPC should be descriptive of its use. The names don't have to be unique, as they are not used for identification by AWS, but they should be to avoid confusion. 

The **CIDR** blocks can be any range of IP addresses with sizes between `/16` and `/28` (65,536 to 16 IP addresses respectively).
The number of IPs should be chosen according to the number of devices that will be included in all the subnets.

It is recommended to use one of the `RFC1918` defined addresses for the VPC CIDR blocks, however any IP range, with size as specified above, can work.
| `RFC1918` range | AWS example range|
| ---             | ---               |
| `10.0.0.0` - `10.255.255.255` (`/8` block) | `10.0.0.0` - `10.0.255.255` (`/16` block) |
| `172.16.0.0` - `176.31.255.255` (`/12` block) | `172.16.0.0` - `172.16.255.255` (`/16` block) |
| `192.168.0.0` - `192.168.255.255` (`/16` block) | `192.168.0.0` - `192.168.255.255` (`/16` block) |

> Note: It should be taken in account that the first three IPs of the VPC block are reserved by AWS for internal use.

Additional tags can be added if needed. 

When the settings are completed, press the 'Create VPC' button

## Subnets
A subnet can be created only after we have created a VPC. We cannot place a subnet inside the default VPC as all the IP ranges were taken by the default subnets.

To create a subnet, first go to the VPC service, then navigate to the 'Subnets' option on the left-side pane. A list of all available subnets is shown.
![Subnet list](media/subnets.png)

## Internet Gateway 
## Routing Tables
## Network ACL

## Security Groups


## EC2

To create an EC2 instance, we first need to go to choose the EC2 option from the AWS services panel.
After choosing the EC2 option, we are presented with a summary panel for all the EC2 instances on the current *Region*. 
At this point, we should switch to the *Region* we want, if it the correct one is not selected. 

We can view a more detailed list of the EC2 instances by clicking the `Instances` option on the left-side panel, or by clicking the summary box for `Instances` or `Instances (running)`.
Both options lead to the same page, but the latter option applies a filter to show only the *running* instances. 
EC2 instances have several states (*running*, *stopped*, *pending*, *terminated*). They are being priced only when they are on a running state. 
As EC2s instances are *Virtual Machines* on the cloud, they require some time to start running after we have provisioned them. During this time, they will be on a `pending` state.

After they complete the provision stage, they will have a private IP for the subnet they are currently in (`default` VPC and subnet if not specified) and a public IP if it was requested.
The EC2 public IP of the EC2 instance may change if it is rebooted, as AWS recycles public IPs when instances are stopped. We can have a specific IP if an **elastic IP** is associated with the instance.
Private IPs do not change, as long as the EC2 instance exists. 

From the *Instances* list, we press the orange button labeled `Create new Instance` to be directed to the EC2 instance creation wizard, where we have to choose the settings for the instance.

1. Image
Firstly we have to choose an image for the machine. 
The image may contain only the baseline operating system, an operating system and a few programs installed, or it can be a custom image we created with all the programs we need on the OS of our choice.
There are several images that are free-tier, including many Linux Ubuntu and Windows operating systems.

2. Provisioning

At this stage, we need to choose the capabilites of the instance. There is a free tier available with a lower CPU and memory capacity.
We can choose that instance for testing purposes.

3. Settings

4. Storage
5. Tags
6. Security Groups
7. Summary
8. Key
As a final step before the instance is launched, a pop-up menu is shown that asks us for the ssh key we would like to choose.
We can create a new key from this menu and download it; or we can use an existing key pair

As an added reminder, a tickbox is included that reminds us to check if the `ssh` key is available in our system.

## Connecting to Instance

## Copying files
We can copy files to our newly created EC2 instance with the `scp` command

## Scenario
