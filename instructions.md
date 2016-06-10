This project is based on http://owaislone.org/blog/webpack-plus-reactjs-and-django/

Prerequisites
-------------

* virtualenv
* virtualenvwrapper
  see http://virtualenvwrapper.readthedocs.org/en/latest/
* nodejs / npm
  install with: 
``` 
     $ sudo apt-get install npm
     $ sudo npm install --upgrade npm 
```
* python-pip
  install with:
```
     $ sudo apt-get install python-pip
```




Setup
-----

** Clone this repository: **
```
git clone https://github.com/HCCB/janus.git janus
```

** Create virtualenv **
```
mkvirtualenv janus
```

** install pip dependencies **
```
cd janus

pip install -r requirements.txt

```

** install JS dependencies **
```
npm install
```


Usage
-----

run on first terminal, so any changes to jsx sources will get bundle:
```
./node_modules/.bin/webpack --config webpack.config.js --watch 
```


