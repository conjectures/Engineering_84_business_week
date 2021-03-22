# GIT and GITHUB

**What is Git and what is it used for?**

Git is version control management software developed by linux kernel developers. 
It is used for collaborative development of source code during software development and for ...

## Setup Guide
Prerequisites:
- Github account

1. **Create a key**
Create an ssh key pair in your local machine and tag your email address to it.
```bash
ssh-keygen -t rsa -b 4096 -C "youremail@example.com"
```
**Important**: The email has to be the same email used in the github

Options used:
  - t: algorithm
  - b: bits used in the encryption hash (more bits means better encryption)

2. **Locate the key**
The new key is located in the `~/.ssh` directory on linux systems. Change working directory there and list the contents.
```bash
cd ~/.ssh
ls
```

3. **Get Public key**
The `ls` command should list the new ssh keys that were generated. Find the public key, which has the suffix `.pub` and copy its contents:
```bash
cat id_ed25519.pub
```
Copy the output of the above command (including the email)

4. **Go to appropriate settings on Github and add the public key**
  - Open your github page, log-in, and then click on the drop down menu on your user icon.
  - From there, select the second to last option **_Settings_**.
  - From Settings, choose the **_SSH and GPG keys_** tab
  - Select the green button **New SSH key**, give it a name and paste the copied key code on the lower box.

  Congratulations! Your SSH key was added.

5. **Create a new repository**
  - Go to your home page and click the green button on the upper left part of the page to create a new repo.
  - Add a name next to the your username. Make sure the name is uniqe from your repositories.
  - Add description if needed. Don't add any other files (README.md, .gitignore, license)
  - (Optional) Select if private or public repo.
  - Create the repository by selecting the green button on the bottom.

6. **Follow steps to create the local repo and then add it to github**

  When the repo is first created, make sure the **SSH** option is selected on the 'Quick setup' box
  Then, on your local machine, change your current directory to the directory you want to have your project.

  Follow the commands on the screen, or use the below guide:
    - Create a `README.md` file by inputing some text in the file.
    ```bash
    echo "# Some title for the project here" >> README.md
    ```
    - Initialize the local git repo
    ```bash
    git init
    ```
    - Add the `README.md` file to the git tracking list.
    ```bash
    git add README.md
    ```
    - Commit your change to the repo and add a simple reference message:
    ```bash
    git commit -m "First commit: add README.md to repo"
    ```
    - Change the branch name to `main` (or leave it as `master`, but use the same branch when pushing)
    ```bash
    git branch -M main
    ```
    - Point git to the online repo (give it the address of the repo we just created on github)
    ```bash
    git remote add origin git@github.com:<username>/<repo_name>.git
    ```
    - Push the local git changes to the online repo. On the first push, the branch has to be specified.
    ```bash
    git push -u origin main
    ```
    - Done!



