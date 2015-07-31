#!/bin/bash

HTTP=$(which http)

if [ ! -x "$HTTP" ]; then
    echo 'You need HTTPie to run this script!'
    echo 'sudo pip3 install httpie'
    exit 1
fi

URL=:8080

set -x

http PUT $URL/pets/1 name=foo animal_type=test
http $URL/pets/1
http PUT $URL/pets/1 name=foo animal_type=test tags:='{"color": "brown"}'
http $URL/pets/1
http $URL/pets animal_type==test
http DELETE $URL/pets/1
