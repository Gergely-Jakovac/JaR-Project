* Html include systems 
  * A quick [overview](https://css-tricks.com/the-simplest-ways-to-handle-html-includes/))
  * Serverside preprocessing with [gulp](https://gulpjs.com/)
  * our own python-based templating system, if we extend it so that it can include files.
* A [note](https://stackoverflow.com/questions/24543101/how-to-create-a-subpage-on-a-website) on page addressing. Also has some other cool insights. 
* Most professional webpages use some html templating language. We could use:
 * [node.js](https://nodejs.org/en/)
  - this is also useful because it can provide serverside math-rendering capacity for MathJax.
 * Our own python program (the other project)
 * [mustache](https://mustache.github.io/). It is similar to our other project (but has different goals)
 * [This](https://colorlib.com/wp/top-templating-engines-for-javascript/) is a list I found.
* Setting up a webserver ([ubuntu tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-16-04))
  * python: we already have it set up, actually. We should configure it so that it returns a html.
  * PHP: [setting up a webserver](https://www.php.net/manual/en/install.php)
    - note that PHP has a lots of html-related tools 
    - PHP was created specificly for web server-programming
