# Sequences

`seq_len()` can be used to get a vector of indices as long as the number
provided  
e.g.

``` r
seq_len(5)
```

    ## [1] 1 2 3 4 5

``` r
vec_length <- 7
seq_len(vec_length)
```

    ## [1] 1 2 3 4 5 6 7

Rather than working out the length of a vector with `length()` and
passing that to `seq_len()`, you can use `seq_along()` and directly
provide the vector.  
e.g.

``` r
seq_along(letters[1:13])
```

    ##  [1]  1  2  3  4  5  6  7  8  9 10 11 12 13

It can also be used with a list, where you get a vector as long as the
number of items in the list.

``` r
seq_along(vector(mode = 'list', length = 7L))
```

    ## [1] 1 2 3 4 5 6 7

For a data.frame you get a vector as long as the number of columns.

``` r
library('palmerpenguins')
ncol(penguins)
```

    ## [1] 8

``` r
seq_along(penguins)
```

    ## [1] 1 2 3 4 5 6 7 8
