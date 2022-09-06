# Render Rmarkdown document to multiple formats with a different name to the default

If you specify multiple formats using the `output_format` option to `render()`, 
and you want the output files to be named something different from the default,
you need to supply a vector of filenames to the `output_file` that is as long 
as the number of different formats.  
e.g.
```r
output_formats <- c('pdf_document', 'html_document', 'word_document')
output_files <- c('newfile.pdf', 
                 'newfile-2.html', 
                 'newfile-3.docx')

render("orig_file.Rmd", output_format = output_formats,
       output_file = output_files)
```

If the base of the output filenames is the same apart from the file extension,
you can just specify the basename, but the vector still needs to be as long as 
the number of formats.

```r
output_formats <- c('pdf_document', 'html_document', 'word_document')
output_files <- rep('newfile', length(output_formats))

render("orig_file.Rmd", output_format = output_formats,
       output_file = output_files)
```
