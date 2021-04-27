# Linux Commands

## Contents
1. [Navigation](#navigation)


## Navigation

The primary way of navigating on Linux systems is with the `cd` command; We can either specify relative path or absolute. 
The absolute path always starts from the root dir `/`. We can specify relative path by naming the directory directly (no `/` required).
If we need more information about where we are, or what directories are in our location, we can use the `pwd` to find our current path, and `ls` to get all the non-hidden directories and files.

We cannot use `sudo` to change directories without implementing a hack. The reason is, `cd` is a builtin command, and so 
We can also use several shortcuts that are listed below:

```
# Change directory to the user's home directory
cd ..

```

