# Linux Commands

> This is not a comprehensive guide!

## Contents
1. [Shell Command Structure](#shell-command-structure)
1. [Linux Streams](#linux-streams)
1. [Navigation](#navigation)
2. [Listing and Searching](#listing-and-searching)
3. [File Viewing and Manipulation](#file-viewing-and-manipulation)
3. [Information](#information)
4. [Process Management](#process-management)
5. [File Permissions](#file-permissions)
6. [Environment Variables](#environment-variables)
7. [Networking](#networking)
4. [Secure Shell and Secure Copy](#secure-shell-and-secure-copy)


## Shell Command Structure
Linux shell commands have a specific syntax.
```bash
[command] [options]
```
The first argument of the statements should be a command, followed by options. The options most often begin with a dash `-` and they may be grouped.
For example the options `-v` and `-f` can be combined into `-vf`, and will have the same function.

GNU systems also offer a more 'verbose' version of a flag, that usually starts with a double dash `--`. For example the flags `-v` and `--verbose` have the same function.
However, there are small differences to the verbose and shorthand versions of the flags. Firstly, the verbose commands cannot be combined with other options. They need to be specified separately.
Additionally, if an input is required for an option, with shorthand flags, the input should be inserted after the flag, separated with a space, but with the longer version, the input might be required after an `=` sign.

If unsure, the `man` command is a useful utility to check proper syntax and available options. To use the `man` command, use the linux shell syntax with `man` as the command, and the query command as option.
For example, if we want the manual for built-in command `ls`, we will type:
```bash
man ls
```
The `man` command uses the `less` utility program to display the information. This means we can search through it by pressing `/` followed by the querystring.
We can exit a `less` program with the `q` button.

## Linux Streams
When a linux command operates, three **streams** are established: `stdin`, `stdout` and `stderr`.

- The `stdin` stream is used as input to a program. It is usually taken from the keyboard input. 

- The `stdout` stream is the output of the program. When a program finishes executing, the `stdout` it outputs is displayed on the terminal.

- Finally `stderr` stream outputs errors from a program and is combined with the `stdout` to be displayed on the terminal. However, it can be redirected for logging purposes.


## Navigation

The primary way of navigating on Linux systems is with the `cd` command; We can either specify relative path or absolute.
The absolute path always starts from the root dir `/`. We can specify relative path by naming the directory directly (no `/` required).
If we need more information about where we are, or what directories are in our location, we can use the `pwd` to find our current path, and `ls` to get all the non-hidden directories and files.

> We can't use `sudo` to change directories. The reason is, `cd` is a builtin command, and `sudo` will look in the path but will not find it there.

We can also use several shortcuts that are listed below:

```bash
# Change directory to the user's home directory
cd ~
cd $HOME
cd

# Change one directory up
cd ..

# Change to previous working directory
cd -

# Print working directory
pwd

# Show directories (not hidden dirs)
ls -d */

```

## Listing and Searching
Many operating systems have aliases for common `ls` commands.
For example, on ubuntu, `ls` is aliased to include colours, or `ll` is an alias of `ls -alF`

We can use the `find` command to list files and directories. 
Find is normally used to find files with the `-name` command, where we can also use the asterisk (`*`) as a wildcard character.

The wildcard means it can be replaced with any other character, and can be used with almost any linux command.

```bash
# List files and directories in current directory
ls
ls --color=auto

# List files and directories, including hidden files (`-a`) on home directory
ls -a ~
ls -a $HOME

# List files, directories, including hidden files (`-a`) in a long listing format, with more information (`-l`). 
# Also classify with `*` for executables, `/` for dirs, `@` for symbolic links, `=` for sockets, `%` for whiteouts and `|` for FIFO
ll
ls -alF

# Find all directories and subdirectories in the current path
find . -type d

# Find all dirs in current path. Restrict to single level depth. Present in long-listing format (`-ls`)
find . -maxdepth 1 -type d -ls

# Count all files and subdirs in your home dir with depth 1
find ~ -maxdepth 1 | wc -l

# Find all textfiles in current directory
find . -maxdepth 1 -name *.txt

```

## File Viewing and Manipulation
A common practice to view the contents of a file is to use `cat`. Normally, `cat` is used to concatenate 
```
# Display file contents

cat


head


# View the last 10 lines of a file
tail filename.txt
tail -n 10 filename.txt
tail --lines 10 filename.txt

# Show last 10 lines of the file, track changes and print them in stdout
tail -F filename.txt

# Sort the lines of the file alphabetically
sort
```
We can even use minimal text editing programs like `nano` and `vim`. Both of them are pre-installed on most Linux distributions so it is useful to know how to use them.
When we enter `nano`, we can view the file contents, edit them, save the file and exit again. The commands are listed on the bottom of the screen. To exit the program without saving changes, press `ctl`+`x` simultaneously.
For `vim` it is more difficult to perform these actions due to its 'modal operation'. By entering different modes, the same keypresses have different functionality. To quickly exit the program, press `esc`, then type `:q!` and press `Enter` to not make any changes.

## Information
```
man
```

## Process Management
```
# Report a snapshot of current processes
ps

# 
# Display linux processes in a dynamic real-time view sorted in terms of CPU usage and display additional info like memory, threads and PID.
top
ps -aux
kill PID
killall process
```
## File Permissions
It is an important security feature in linux, that not all users can have access permission to certain files. 
Each file or directory has permissions based on user groups, called **Permission Groups**. The groups are split into `owner`, `group`, and `all users`.
These permissions are applying to the person that owns the file, the group that the file has been assigned, and all other users accordingly.

Each of these groups has a different *Permission Type*: `read`, `write` and `execute`.

flags `777`, `400`, `600`, `r`, `w`, `x`
![Permission Flags](permission-flags.png)
```
chmod
```

## Environment Variables 
```
env
```
## Networking

## Secure Shell, Secure Copy
We can use `ssh` to connect to a remote host. The connections are encrypted, so before we establish a connection, a key pair has to be created, and the public key exchanged
Additional settings can be addes to the `ssh` command with the `-o` flag.
Some useful settings are `ForwardAgent`, `StrictHostKeyChecking`, etc.

The keys should be stored in `~/.ssh` directory, as ssh will search there first. If the key is located somewhere else, we need to specify it with the `-i` flag.
```
ssh
```

We can add a `config` file inside the `~/.ssh` dir. Example
```
Host <hostname>
  Hostname <IP>
  User <username>
  ...
```
Additionally, we can add commands to be executed to the remote host with the following syntax:
```bash
ssh <user>@<host-address> << 'EOF'
  # commands here
EOF
```
With the configuration file, we can add settings to the `ssh` connection without specifying them with the `-o` flag
```
scp -i IdentityFile.pem filename user@ip:/[path]
```

