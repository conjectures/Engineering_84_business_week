# Git Intermediate

## Git stages
When on your localhost and working in a git repository, the git workflow will be split in three **stages**:

- **Modified**

Assuming that `git` is already set up and initialised in a directory, any files not included in the `.gitignore` file that are modified will be in the **Modified** list. 
This means that git knows that the file was the file has some differences when compared to the original code. However it doesn't know what those changes are.
The files that are modified can be seen with the `git status` command in red colour.

- **Staged**

After editing the a file, we want to tell git to track its changes. This means, a `diff` file will be created to store the differences between the modified and original versions of a file.
Storing the differences is much more efficient, when compared to storing the whole file. This makes git remote updating much faster.
To add a file in the **Staging Area** we use the `git add` command. We can specify one or more files to be added, or the whole directory:
```bash
# Track files1 and file2
git add file1 file2
# Track all files in working directory
git add .
```

- **Commited**

When we have made all the changes we want to, we want to commit those changes. This means that we are ready to push the work that we have made, as we don't have anything else to add at the moment.
When commiting, we add a small message to describe the changes that we have made. This message can also be thought of as an alternative 'identifier' of the commitment and can be seen in the commit history along with the actual identifier.
To add the staged files to the **Commit Area**, we need to use the `git commit` command.
```bash
# Commit staged files with a message
git commit -m 'message '
```
At this point we can push the commit to our remote server, or we can follow the cycle again. If the latter is the case, when it comes time to push the changes, we need to push the older commit first. 


## Reseting Stage Area

There may be a point where we made a wrong addition to our staging area. We can remove a single file from being tracked, or reset the whole staging.
```bash
# Remove file from staging area
git reset HEAD <file>

```


