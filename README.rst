==============================
Connexion Example REST Service
==============================

This example application implements a very basic "pet shop" REST service using the `Connexion`_ Python library.

Connexion is a framework on top of Flask_ to automagically handle your REST API requests
based on `Swagger 2.0 Specification`_ files in YAML.


Features
========

This example application shows various features supported by the Connexion library:

* mapping of REST operations to Python functions (using the ``operationId`` in ``swagger.yaml``)
* bundled Swagger UI (served on `/ui/`_ path)
* automatic JSON serialization for ``application/json`` content type
* schema validation for the HTTP request body:

  * required object properties
  * primitive JSON types (string, integers, etc)
  * date/time values
  * string lengths

* gevent WSGI server


Files
=====

The example application only needs very few files:

* ``swagger.yaml``: the pet shop REST API Swagger definition
* ``app.py``: implementation of the pet shop operations with in-memory storage
* ``requirements.txt``: list of required Python libraries
* ``Dockerfile``: to build the example as a runnable Docker image
* ``test.sh``: shell script to execute example HTTP requests against the pet shop API


Running Locally
===============

You can run the Python application directly on your local operation system:

.. code-block:: bash

    $ sudo pip3 install -r requirements.txt
    $ ./app.py # start the HTTP server
    $ xdg-open http://localhost:8080/ui/
    $ ./test.sh # do some test HTTP requests


Running with Docker
===================

You can build the example application as a Docker image and run it:

.. code-block:: bash

    $ docker build -t connexion-example .
    $ docker run -d -p 8080:8080 connexion-example
    $ ./test.sh # do some test HTTP requests

.. _Connexion: https://pypi.python.org/pypi/connexion
.. _Flask: http://flask.pocoo.org/
.. _Swagger 2.0 Specification: https://github.com/swagger-api/swagger-spec/blob/master/versions/2.0.md
.. _/ui/: http://localhost:8080/ui/
