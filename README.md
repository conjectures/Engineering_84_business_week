# Linux Commands

> This is not a comprehensive guide!

## Contents
1. [Navigation](#navigation)
2. [Listing and Searching](#listing-and-searching)
3. [Information](#information)
4. [Process Management](#process-management)
5. [Permission](#permission)
6. [Environment Variables](#environment-variables)
7. [Networking](#networking)
4. [Secure Shell and Secure Copy](#secure-shell-and-secure-copy)


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

We can use the `find` command to list files and directories. Find is used to search for 
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

```
## Information
```
man
head
tail
```
## Process Management
```
top
ps
ps -aux
kill PID
killall process
```
## Permission
flags `777`, `400`, `600`, `r`, `w`, `x`
```
chmod
```

## Environment Variables 
```
env
```
## Networking

## Secure Shell, Secure Copy


