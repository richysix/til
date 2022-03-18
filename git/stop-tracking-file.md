# Stop tracking a file and remove it from the repository

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