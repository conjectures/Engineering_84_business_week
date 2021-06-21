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


## Resetting
### Resetting Unstaged Changes
We can easily revert our changes with two commands,the `git clean` and the `git checkout` command. The first command removes untracked files from the working tree,
while the latter will create a 'temporary' branch to track our change, therefore removing it from our stack. The branch is not 'saved' and so the changes are lost.

We can view the files that will be removed from the stack with the `git clean` command with the `-n` flag:
```bash
# Show files to be removed
git clean -n
```
Then we can use the two commands to remove the files:
```bash
# Remove untracked files
git clean -f

# Remove untracked changes to tracked files
git checkout -- <file>
# Remove untracked changes from all tracked files (in current dir)
git checkout -- .
```
### Reseting Stage Area

There may be a point where we made a wrong addition to our staging area. We can remove a single file from being tracked, or reset the whole staging.
```bash
# Remove file from staging area
git reset HEAD <file>

# Remove all files from staging area
git reset HEAD
```

### Reseting Local Commit
Perhaps we have made some changes that need to be reverted, but they have already been commited.
That is, the changes are no longer in the sraging area, and the local repo `HEAD` has already been altered.
Suppose also that the remote repository hasn't been updated with these changes, meaning that we haven't pushed the bad commit yet.

We can revert back to the previous commit by just reverting the `HEAD` to the previous commit.
To do this we use:
```bash
git reset HEAD~1
```

## Fork
Forking is the action of making a repo copy for your own use.
This may sound very similar to a `git clone`, however, with `fork` the repo copy is performed on the server.
The original repo contributors may not be able to push code on the forked repo without your approval, since the owner is yourself.

Forking  the repo is useful for many occasions.
Firstly, if a contributor wants to work on an issue without impacting the original repo, or if he doesn't have permissions to push, he can go ahead and fork it.
He can then perform the changes he wants and later ask for the original repo owner to 'merge' it.

Additionally, forking a repo could be a part of the collaborative development process for a team project.
Each member could have their own, fork of the main project that they work on, and their changes could be automatically or manually be merged after testing and approval.


## Merging
Merge is the process of combining branches of a repository. The branches could be different versions of the same branch, or they could be an unrelated branch altogether.

```
# Fetch the latest changes (of all branches) on repo located at <remote> address
git fetch <remote>

# Merge current branch with 
git merge <branch>
```

## Pulling
Pull is not a single operation. It consists of, in order, the `fetch` and `merge` commands.
So when a `pull` command is implemented, git will `fetch` the differences from the`origin/main` branch of the repo. Then, it will try to merge our current branch with `origin/main`.
If `git` sees that there are changes, either unstaged, or staged, it will cancel the operation, as it doesn't know how to merge the conflicts. 

### Pull and merge without caring about local changes


### Pull but you care about local changes

### Download remote differences but do not apply them yet

## Workflows

### Personal Repository Workflow
### Collaborative Workflow
