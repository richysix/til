# Remove comment characters from Rmarkdown output

I discovered this [here](https://stackoverflow.com/questions/74224443/rmarkdown-read-code-from-file-and-display-with-highlight) while looking up how to do somethng else.
It's also documented [here](https://bookdown.org/yihui/rmarkdown-cookbook/opts-comment.html).

By default, R code output has two hashes `##` inserted in front of test output.
This is so that if code and results are being output together, you can copy and paste that whole thing into the R console and the output will be ignored because it is commented out.

To remove the hashes, you can use the `comment` chunk option in the chunk header.  
e.g. `comment = ""`

So if you have a chunk like this

    ```{r echo=FALSE, comment=""}
    cat("Verbatim output")

    2 + 2
    ```

The output would be just 

```
Verbatim output
```
```
[1] 4
```

The [1] appears in the output because 2 + 2 produces a vector of length one.
