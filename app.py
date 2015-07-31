#!/usr/bin/env python3
import connexion
import datetime
import flask
import logging


# our memory-only pet storage
PETS = {}


def get_pets():
    animal_type = flask.request.args.get('animal_type')
    return [pet for pet in PETS.values() if not animal_type or pet['animal_type'] == animal_type]


def get_pet(pet_id):
    pet = PETS.get(pet_id)
    return pet or ('Not found', 404)


def put_pet(pet_id):
    exists = pet_id in PETS
    pet = flask.request.json
    pet['id'] = pet_id
    if exists:
        logging.info('Updating pet %s..', pet_id)
    else:
        logging.info('Creating pet %s..', pet_id)
        pet['created'] = datetime.datetime.utcnow()
    PETS[pet_id] = pet
    return None, (200 if exists else 201)


def delete_pet(pet_id):
    if pet_id in PETS:
        logging.info('Deleting pet %s..', pet_id)
        del PETS[pet_id]
        return None, 204
    else:
        return None, 404


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app = connexion.App(__name__, port=8080, debug=True, server='gevent')
    app.add_api('swagger.yaml')
    app.run()
