# Teardown a Vagrant Environment

## Suspend
This is the fastest option to restart. Uses more disk space.
```bash
vagrant suspend
```

## Halt
The shuts down the virtual machine, so does not save the contents of the machine's RAM.
It will take longer to start up again, but takes up less disk space.
```bash
vagrant halt
```