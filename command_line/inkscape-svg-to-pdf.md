# Convert inkscape svg to pdf

```bash
for file in *.svg; do
    filename=$(basename "$file")
    dir=$( dirname $file )
    inkscape "$file" --export-type=pdf --export-area-page --export-dpi=300 \
    -o "$dir/${filename%.svg}.pdf"
done
```

Depending on which you want to do, you can use either `--export-area-page` or `--export-area-drawing`
