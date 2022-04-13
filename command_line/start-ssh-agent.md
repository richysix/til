# Start ssh-agent so that ssh-add works

If you try to add an ssh key and you get this error  
`Could not open a connection to your authentication agent`

You need to eval the output from the shh-agent command
```bash
eval "$(ssh-agent)"
```
