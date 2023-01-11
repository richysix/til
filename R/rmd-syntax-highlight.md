# Create a file with code and then display that file with syntax highlighting in Rmarkdown

This comes from [here](https://stackoverflow.com/questions/74224443/rmarkdown-read-code-from-file-and-display-with-highlight)

Sometimes, in an Rmarkdown document, I want to create a file using code so that it's reproducible, but I also want to disply the contents of that file with syntax highlighting in the rendered document.

You can do this by creating the file in one chunk and then reading it in using another chunk with `comment=""` and using the `class.output` option for syntax highlghting

e.g.

    ```{bash echo=FALSE}
    echo "import time

    print("Going to sleep")
    time.sleep(2)
    print("Awake again")" > sleep_test.py
    ```

    ```{bash sleep_test, echo=FALSE, class.output="python", comment=""}
    cat sleep_test.py
    ```

The syntax highlighting is done by `pandoc`. To find out which languages `pandoc` supports syntax highlighting for, you can run this.
```
pandoc --list-highlight-languages
```