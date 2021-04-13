# Vagrant Task: Multi Machine Setup
> Time: 120 - 180'

## Summary
The sample application has the ability to connect to a database. 
We need to provision our development environment with a Virtual Machine for the database and one for the Database.

Vagrant is capable of running two or more virtual machines at once with different configurations.

## Tasks
- Research how to create a multi-machine Vagrant environment.
- Add a second virtual machine called "db" to your Vagrant file
- Configure the db machine with a different IP from the app
- Provision the db machine with a MongoDB database

## Notes
When you have the second machine running, further configuration of the app is required to make use of the database. 
We will cover this in the next lesson.

You can test if your database is working correctly by running the test suite in the test folder. 
There are two sets of tests. One for the app VM and one for the db VM. Make them all pass.

```bash
# Test the app
cd test
rake spec
```
## Acceptance Criteria
- Uses vagrant file
- Create 2 VM APP and Mongod
- Localhost set to development.local
- App works on Port 3000 (development.local:3000)
- Work with only command "vagrant up" &/or mininum commands

- If all tests succeed, it should work on the url `/posts` as well as `/fibonacci/30` 
- Additionally, documentation should exist in the README.md file.
  Documentation includes: Intro (purpose of repo), Pre Requisits and Intructions
  Instructions have a clear step by step. 
- Repo exists on github


## Documentation


## Solution
To enable multi-machine Vagrant deployment, we need to create two different boxes in the Vagrantfile

