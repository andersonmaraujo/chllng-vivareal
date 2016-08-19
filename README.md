Foi desenvolvido em OSX 10.11
Python 2.7.10

Terminal:

$ sudo pip install flask
$ sudo pip install requests
$ sudo pip install voluptuous
-------------------------------------


Na pasta da aplicação

Os dados já estão pré-inseridos, mas 
caso queiram reiniciar a base, basta:

$ python 

>>> from database import init_db
>>> init_db()
>>> exit()
-------------------------------------

Para rodar a aplicação

$ python vivareal.py
-------------------------------------


A aplicação ficará disponível em:

http://127.0.0.1:5000/