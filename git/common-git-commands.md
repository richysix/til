# Common git commands

## Checkout a tracking branch from a remote repository

```
git switch -c branch_name --track remote/branch_name
```

e.g.
```
git switch -c task/parser_interface_upgrade --track origin/task/parser_interface_upgrade
```

## List all the files being tracked in a repository

```bash
git ls-tree -r master --name-only
```

## Find out when a file was added to a repository

from [this answer](https://stackoverflow.com/questions/11533199/how-to-find-the-commit-in-which-a-given-file-was-added)

To find the commit when a file was added use:
```
git log --diff-filter=A -- filename
```

Adding `--follow` will also find files that have been renamed, assuming the 
files have not changed too much
```
git log --follow --diff-filter=A -- filename
```

## Add a tag to a specific commit

To tag an old commit use `git tag`
```bash
git tag -a TAGNAME -m "MESSAGE" COMMITID
```
e.g.
```bash
git tag -a v0.0.0.9004 -m "Bugfix in svg arguments" 60dd13d
```

Then push all tags up
```
git push --tags
```

## Stop tracking a file and remove it from the repository

from https://stackabuse.com/git-stop-tracking-file-after-adding-to-gitignore

If you've added a file to your repository and now you want to stop tracking it,
but leave it in the directory and ignore it with .gitignore.

First add the file to `.gitignore`
```bash
echo "file.txt" >> .gitignore
```

Then stop tracking the file
```
git rm --cached file.txt
```
The `--cached` flag removes it from the git index, but not from the working directory.

## Remove a file completely from a repository

To remove a file from a repository and all the history of a repository, you
can use a tool called [`git-filter-repo`](https://github.com/newren/git-filter-repo/).
**This will rewrite the complete history of the repo!**

To install download from the git repository and make sure it is in the PATH
```
cd ~/bin/
wget https://raw.githubusercontent.com/newren/git-filter-repo/main/git-filter-repo
```

For example, to remove a file called large-file.tsv
```
git filter-repo --path large-file.tsv --invert-paths
```

`--path` specifies paths to retain in the filtered repo and `--invert-paths` 
changes from including those files to exlcuding them. Mulitple files can be
removed at once
```
git filter-repo --path file1 --path file2 --invert-paths
```
