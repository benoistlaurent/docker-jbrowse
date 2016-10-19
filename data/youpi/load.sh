#!/bin/bash

rm -rf $JBROWSE_DATA/*

mkdir -p $JBROWSE_DATA/raw/
ln -s $DATA_DIR/youpi/ $JBROWSE_DATA/raw/youpi
ln -sf $DATA_DIR/youpi.json $JBROWSE_DATA/raw/

prepare-refseqs.pl --fasta $DATA_DIR/youpi/youpi.fa --out $JBROWSE_DATA
biodb-to-json.pl -v --conf $DATA_DIR/youpi.json --out $JBROWSE_DATA

cat $DATA_DIR/youpi/youpi.gff3.conf                >> $JBROWSE_DATA/tracks.conf

generate-names.pl --safeMode -v --out $JBROWSE_DATA


