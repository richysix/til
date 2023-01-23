# Find out when a file was added to a repository

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