# my-cv
Simple CV hosted on github-pages


### To install jekyll:


[https://jekyllrb.com/docs/installation/](https://jekyllrb.com/docs/installation/)


### To create site:


```
bundle init
bundle add github-pages
bundle update
bundle exec jekyll build
bundle exec jekyll serve
```


Site will be hosted locally, and all site data will be in the ```_site``` folder.

Push the contents of this folder to the ```online-cv``` repository.

Local host at: http://0.0.0.0:4000/ajaspan-cv/

CV will then be found at [https://aejaspan.github.io/ajaspan-cv/index.html](https://aejaspan.github.io/ajaspan-cv/index.html)


make pdf from 

https://wkhtmltopdf.org/usage/wkhtmltopdf.txt

```
wkhtmltopdf --no-print-media-type --enable-plugins --title AEJaspanCV --viewport-size 800 -B 5 -L 0 -R 0 -T 5 --footer-right "[page]/[topage]" --footer-font-name Roboto --footer-font-size 9 http://0.0.0.0:4000/ajaspan-cv/ AEJaspan-CV.pdf

wkhtmltopdf --no-print-media-type --enable-plugins --title AEJaspanCV --viewport-size 800 -B 5 -L 0 -R 0 -T 5 --footer-right "[page]/[topage]" --footer-font-name Roboto --footer-font-size 9  https://aejaspan.github.io/ajaspan-cv/index.html AEJaspan-CV.pdf

-- ususally has to be ran twice
```

<!-- #https://stackoverflow.com/questions/34479040/how-to-install-wkhtmltopdf-with-patched-qt -->