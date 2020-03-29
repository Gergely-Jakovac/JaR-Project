* A [note](https://stackoverflow.com/questions/24543101/how-to-create-a-subpage-on-a-website) on page addressing. Also has some other cool insights. 
* Most professional webpages use some html templating language. Also, we need an html include system. THese two goals could be achieved with the same tool. We could use:
  * our own python-based templating system, if we extend it so that it can include files.
  * Serverside preprocessing with [gulp](https://gulpjs.com/). Gulp can only handle incudes, not templating.
  * PHP. PHP can do everything we need on a server.
  * [django](https://www.djangoproject.com/): a "high-level powerful Python Web Frame work". Can handle everything we need.
    - It is really python-like.
    - We must structure our code the django-way.
    - Focuses on templting. It is NOT a server language.
  * [node.js](https://nodejs.org/en/)
    - this is also useful because it can provide serverside math-rendering capacity for MathJax.
    - node.js can handle much more than just templating
  * [mustache](https://mustache.github.io/). It is similar to our python project (but has different goals)
  * A quick [overview](https://css-tricks.com/the-simplest-ways-to-handle-html-includes/)) of including systems.
  * [This](https://colorlib.com/wp/top-templating-engines-for-javascript/) is a list of html (javascript) templatng tools I found.
* Setting up a webserver ([ubuntu tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-16-04))
  * python: we already have it set up, actually. We should configure it so that it returns a html.
  * PHP: [setting up a webserver](https://www.php.net/manual/en/install.php)
    - note that PHP has a lots of html-related tools 
    - PHP was created specificly for web server-programming
