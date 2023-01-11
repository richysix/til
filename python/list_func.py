import re

def filter_list(items):
    filtered_list = []
    for x in items:
        if re.search('cat', x) is not None:
            filtered_list.append(x)
    return(filtered_list)
