#! /bin/bash

VENV_NAME=.venv-goodkitties
python3 -m venv ${VENV_NAME}

. ./${VENV_NAME}/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

# Hint how to activate
echo . ./${VENV_NAME}/bin/activate



