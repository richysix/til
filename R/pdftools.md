``` r
library('pdftools')
library('palmerpenguins')
library('ggplot2')
```

The `pdftools` package can be used to split and combine pages from pdfs.

``` r
# create a test pdf
pdf('test-all.pdf')
ggplot(data = penguins) +
  geom_point(aes(x = bill_length_mm, y = bill_depth_mm))
ggplot(data = penguins) +
  geom_histogram(aes(x = body_mass_g))
ggplot(data = penguins) +
  geom_boxplot(aes(x = species, y = body_mass_g))
ggplot(data = na.omit(penguins)) +
  geom_boxplot(aes(x = species, y = body_mass_g, fill = sex)) +
  scale_fill_brewer(palette = 'Dark2')
dev.off()
```

    ## quartz_off_screen 
    ##                 2

To produce a separate pdf file for each page, use `pdf_split`.

``` r
pdf_split('test-all.pdf', output = 'test-split')
```

    ## [1] "test-split_0001.pdf" "test-split_0002.pdf" "test-split_0003.pdf"
    ## [4] "test-split_0004.pdf"

To create a new pdf with a subset of the pages, use `pdf_subset`

``` r
pdf_subset('test-all.pdf', pages = 1:2, output = 'test-subset-1.pdf')
```

    ## [1] "/Users/rjw26/checkouts/til/R/test-subset-1.pdf"

``` r
pdf_subset('test-all.pdf', pages = 3:4, output = 'test-subset-2.pdf')
```

    ## [1] "/Users/rjw26/checkouts/til/R/test-subset-2.pdf"

To combine several pdfs into one, use `pdf_combine`

``` r
pdf_combine(c('test-subset-2.pdf', 'test-all.pdf', 'test-subset-1.pdf'),
            output = 'test-combined.pdf')
```

    ## [1] "/Users/rjw26/checkouts/til/R/test-combined.pdf"
