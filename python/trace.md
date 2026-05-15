# Using trace to show line by line execution of python script

You can use the trace module to show what lines are being executing when a python script is run. See [docs page](https://docs.python.org/3/library/trace.html)

```
python -m trace -t script.py
```

`-t, --trace` show lines as they are executed

`-c, --count` produces a count of how many times each statement was executed
