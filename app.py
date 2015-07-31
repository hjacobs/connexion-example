#!/usr/bin/env python3
import connexion
import flask
import logging


PETS = {}


def get_pets():
    return PETS.values()


def get_pet(pet_id):
    return PETS[pet_id]


def put_pet(pet_id):
    PETS[pet_id] = flask.request.json


def delete_pet(pet_id):
    del PETS[pet_id]


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app = connexion.App(__name__, port=8080, debug=True, server='gevent')
    app.add_api('swagger.yaml')
    app.run()
