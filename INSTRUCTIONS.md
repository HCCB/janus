This project is based on http://owaislone.org/blog/webpack-plus-reactjs-and-django/

Prerequisites
-------------

* python-pip

  install with:

```
     $ sudo apt-get install python-pip
```


* virtualenv

* virtualenvwrapper

  see http://virtualenvwrapper.readthedocs.org/en/latest/
  create virtualenv for janus, e.g.:
```
     $ mkvirtualenv janus
     $ setvirtualenvproject # run this to set the directory...
```


* nodejs / npm

  install with:
  (NB: you normally should **NOT** run script directly off the internet)

``` 
     $ sudo apt-get purge npm nodejs nodejs-legacy
     $ sudo apt-get install nodejs
     $ sudo npm install -g --upgrade npm 
```

  for those using proxy (apt-proxy, etc) you may need to add the following:

```
     Acquire::http::Proxy { deb.nodesource.com DIRECT; };
```

  to your apt proxy configuration.  (usually found in /etc/apt/apt.conf.d/<*>proxy)


* babel

  install babel global, babel does not like to be installed locally:

```
     $ sudo npm install -g babel
```

Setup
-----

** Create virtualenv **

```
    $ mkvirtualenv janus
```

** Clone this repository: **

```
    $ git clone https://github.com/HCCB/janus.git janus
    $ cd janus
    $ setvirtualenvproject
```
    The ```setvirtualenvproject``` is a command from virtualenvwrapper that will set the default directory of the project to the current directory.  So, whenever you ```workon janus```, your current directory is set to the directory remembered with ```setvirtualenvproject```.


** install JS dependencies **

```
    $ npm install
```

** install pip dependencies **

```
    $ pip install -r requirements.txt

```


Usage
-----

On one terminal run:
```
    $ npm start
```

On another terminal run:
```
    $ cd src/janus
    $ ./manage.py runserver
```

open browser at http://localhost:8000 

You can now edit the javascript files, and have it reflected into the browser without a refresh.  Of course, if you make changes that has errors, you may still need to refresh your browser.


