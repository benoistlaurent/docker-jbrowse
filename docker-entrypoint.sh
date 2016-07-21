#!/bin/bash

export JBROWSE_DATA=/jbrowse/data
export JBROWSE=/jbrowse
export DATA_DIR=/data

[ -f $DATA_DIR/load.sh ] && . $DATA_DIR/load.sh

nginx -g "daemon off;"
