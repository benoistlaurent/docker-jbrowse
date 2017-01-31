#!/bin/bash

export JBROWSE_DATA=/jbrowse/data
export JBROWSE=/jbrowse
export DATA_DIR=/data

[ -f $DATA_DIR/Makefile ] && make -f $DATA_DIR/Makefile

nginx -g "daemon off;"
