#!/usr/bin/env bash

PYTHON_LOCATION=$(which python3)

$PYTHON_LOCATION -m nuitka --help >/dev/null
if [ $? -eq 1 ]; then
    echo "Installing nuitka"
    $PYTHON_LOCATION -m pip install nuitka
    if [ $? -eq 1 ]; then
        curl https://bootstrap.pypa.io/get-pip.py
        $PYTHON_LOCATION ./get-pip.py
        rm -rf get-pip.py
    fi
    $PYTHON_LOCATION -m pip install nuitka
fi

$PYTHON_LOCATION -m nuitka --follow-imports --standalone main.py

#TODO: add moving to /usr/bin
