# Provide default values for argparse arguments

From this [answer](https://stackoverflow.com/questions/12151306/argparse-way-to-include-default-values-in-help)

`argparse.ArgumentParser` has a formatter_class option for formatting the help text produced.

One of the available classes is `argparse.ArgumentDefaultsHelpFormatter` which includes the default value for all arguments that have help text defined.

e.g.

```python
parser = argparse.ArgumentParser(
    description='Script to do something',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--sleep_interval', default=600,
    metavar='Int', type = int, 
    help='Set length of interval between actions')
args = parser.parse_args()
```

would have help text like this

    usage: argparse-test.py [-h] [--sleep_interval Int]

    Script to do something

    optional arguments:
    -h, --help            show this help message and exit
    --sleep_interval Int  Set length of interval between actions (default: 600)

