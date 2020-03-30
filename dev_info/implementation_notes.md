* A [note](https://stackoverflow.com/questions/24543101/how-to-create-a-subpage-on-a-website) on page addressing. Also has some other cool insights. 
* Most professional webpages use some html templating language. Also, we need an html include system. These two goals could be achieved with the same tool. We could use:
  * our own python-based templating system, if we extend it so that it can include files.
  * Serverside preprocessing with [gulp](https://gulpjs.com/). Gulp can only handle incudes, not templating.
  * PHP. PHP can do everything we need on a server.
  * [django](https://www.djangoproject.com/): a "high-level powerful Python Web Frame work". Can handle everything we need.
    - It is really python-like.
    - We must structure our code the django-way.
    - Focuses on templating. It is NOT a server language.
  * [node.js](https://nodejs.org/en/)
    - also useful because it can provide serverside math-rendering capacity for MathJax.
    - node.js can handle much more than just templating
  * [mustache](https://mustache.github.io/). It is similar to our python project (but has different goals)
  * A quick [overview](https://css-tricks.com/the-simplest-ways-to-handle-html-includes/)) of including systems.
  * [This](https://colorlib.com/wp/top-templating-engines-for-javascript/) is a list of html (javascript) templatng tools I found.
* Setting up a webserver:
  * python: we already have it set up, actually. We should configure it so that it returns a html.
  * PHP: [setting up a webserver](https://www.php.net/manual/en/install.php)
    - note that PHP has a lots of html-related tools 
    - PHP was created specificly for web server-programming
* Getting our page to the World Wide Web: **a [tutorial](https://www.thesitewizard.com/gettingstarted/startwebsite.shtml) on how to set up a website.**
  * [The things](https://www.quora.com/How-do-I-upload-a-website-to-the-world-wide-web-Give-instructions-about-domain-name-hosting-plans-Can-anybody-answer-this-in-a-clear-concise-manner) we need to do.
  * At first, we should set up the page on our computer. [Posible problems](https://www.website.com/beginnerguide/webhosting/6/7/can-i-host-my-website-on-my-personal-computer?.ws). [Apache](https://httpd.apache.org/).[Ubuntu tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-16-04).
  * [Domain registration info](https://www.thesitewizard.com/archive/registerdomain.shtml). Basicly everything that we need is listed here. The most used [domain name-registrar.](https://uk.godaddy.com/)
  * [Tips on domain name choosing](https://www.thesitewizard.com/archive/domainname.shtml), 

* Notes on how to handle an account:
  * [Google login](https://developers.google.com/identity/sign-in/web/sign-in) tutorial.
    - [another](https://developers.google.com/identity/sign-in/web) google login tutorial.
  * css [login tutorial](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_login_form_modal).
  * css [sihn up form tutorial](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_signup_form).
  * a [note](https://security.blogoverflow.com/2013/09/about-secure-password-hashing/) on password hashing.
  * a [javascript implementation](https://github.com/ricmoo/scrypt-js) of the scrypt hashing algorithm. And [here](https://github.com/tonyg/js-scrypt) is another one. [Here](https://blog.filippo.io/the-scrypt-parameters/) is a discussion of scyrpt parameters.
