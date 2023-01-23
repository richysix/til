# Remove a file completely from a repository

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
