# Including specific files with rsync

## Copying certain files and directories recursively

Say you have a directory hierarchy and you want to replicate the directory
structure and copy some (e.g. pdf files), but not all the files within the
structure.
The first filter option includes any files ending in pdf. The second one is
required to include directories below the top one. Otherwise they would be
excluded by the last rule and would never be searched. When all the
sub-directories are included the last rule then excludes any file that doesn't
match the first rule (i.e. any file that isn't a pdf file)

```
rsync -avz --filter "+ *.pdf" --filter "+ */" --filter "- *" source:directory dest:directory
```

From [this question](https://unix.stackexchange.com/questions/2161/rsync-filter-copying-one-pattern-only) on Stack Exchange
