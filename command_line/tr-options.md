# Options to `tr`

`-d string1` deletes all occurences of string1

e.g.
```
echo '   aaabb  b   ccc' | tr -d '[:space:]'
aaabbbccc
```

`-s string1` replaces consecutive occurences of characters in string1 with a single occurence

e.g.
```
echo 'aaabbbccc' | tr -s ab
abccc
```

`-ds string1 string2` combination of -d and -s. Characters in string1 are deleted first and then those from string2 squeezed

e.g.
```
echo '   aaabb  b   c c c c' | tr -ds '[:space:]' abc
abc
```
