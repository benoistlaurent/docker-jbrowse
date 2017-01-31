#!/bin/bash

git pull
make -f $CV11_DATA_DIR/Makefile clean &&\
make -f $CV11_DATA_DIR/Makefile install
