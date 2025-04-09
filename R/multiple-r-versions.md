# Installing mutliple version of R on MacOS

This was prompted by this [blog post](https://jacobrprice.github.io/2019/09/19/Installing-multiple-parallel-R-versions.html)

The post has most of the information you need but exactly which packages to 
forget changes with different version of MacOS.

To find which packages are installed relating to R run
```
sudo pkgutil --packages | grep -i 'r-project'
```

As it says in the [Uninstalling under MacOS](https://cran.rstudio.org/doc/manuals/R-admin.html#Uninstalling-under-macOS) 
section of the R Installation and Administration document, the R domain is 
named inconsistently so you have to use the `-i` option to grep to search 
case-insensitively.

In my case the packages are not the same as those shown in the original blog post.
They are similar to those named in [Uninstalling under MacOS](https://cran.rstudio.org/doc/manuals/R-admin.html#Uninstalling-under-macOS),
except with `x86_64` instead of `arm64` because I have an Intel Mac.
```
org.R-project.x86_64.R.fw.pkg
org.R-project.x86_64.R.GUI.pkg
org.r-project.x86_64.tcltk
org.r-project.x86_64.texinfo
```

It does in fact mention that in [Uninstalling under MacOS](https://cran.rstudio.org/doc/manuals/R-admin.html#Uninstalling-under-macOS),
but I didn't see it originally.

Anyway with those package names I can now run 
```
sudo pkgutil \
--forget org.R-project.x86_64.R.fw.pkg \
--forget org.R-project.x86_64.R.GUI.pkg \
--forget org.r-project.x86_64.tcltk \
--forget org.r-project.x86_64.texinfo
```

I have a script to get currently installed packages and install new ones 
from a list, similar to the one in the blog post.
To get a list of installed packages before updating, I run
```
cd ~/checkouts/scripts
Rscript UpdatedRVersion-Install-Packages.R --get_packages installed-packages-r4.3.tsv
```

And then install the newest version of R without overwriting the current one.

Now, re-install packages. The `installed-packages-r4.3.tsv` file created above 
is the input to the `UpdatedRVersion-Install-Packages.R`. If there are packages 
that you don't want to reinstall, simply delete that line from the file.
```
Rscript UpdatedRVersion-Install-Packages.R installed-packages-r4.3.tsv
```
