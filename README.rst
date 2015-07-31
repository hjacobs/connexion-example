==============================
Connexion Example REST Service
==============================

Running Locally
===============

.. code-block:: bash

    $ sudo pip3 install -r requirements.txt
    $ ./app.py # start the HTTP server
    $ xdg-open http://localhost:8080/ui/
    $ ./test.sh # do some test HTTP requests

Running with Docker
===================

.. code-block:: bash

    $ docker build -t connexion-example .
    $ docker run -it -p 8080:8080 connexion-exampl
