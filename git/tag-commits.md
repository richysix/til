# Add a tag to a specific commit

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
