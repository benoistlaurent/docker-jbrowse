#!/bin/bash

#
# Install data to JBrowse data directory.
# 
# This script assumes that those environment variables are adequatly set:
#   - JBROWSE_DATA: path to JBrowse data directory
#   - DATA_DIR: path to the directory where are cv11.json.in and cv11 directory
#

rm -rf $JBROWSE_DATA/*

mkdir -p $JBROWSE_DATA/raw/
ln -s $DATA_DIR/cv11/ $JBROWSE_DATA/raw/cv11
sed 's#@DATA_DIR@#'"$DATA_DIR"'#' $DATA_DIR/cv11.json.in > $JBROWSE_DATA/raw/cv11.json

prepare-refseqs.pl --fasta $DATA_DIR/cv11/cv11.fa --out $JBROWSE_DATA
biodb-to-json.pl -v --conf $JBROWSE_DATA/raw/cv11.json --out $JBROWSE_DATA

cat $DATA_DIR/cv11/directional_WTSS_RPM_strand+.bw.conf     >> $JBROWSE_DATA/tracks.conf
cat $DATA_DIR/cv11/directional_WTSS_RPM_strand-.bw.conf     >> $JBROWSE_DATA/tracks.conf
cat $DATA_DIR/cv11/sRNASeq_RPP_avRPM_strand+.bw.conf        >> $JBROWSE_DATA/tracks.conf
cat $DATA_DIR/cv11/sRNASeq_RPP_avRPM_strand-.bw.conf        >> $JBROWSE_DATA/tracks.conf
cat $DATA_DIR/cv11/sRNASeq_mock_avRPM_strand+.bw.conf       >> $JBROWSE_DATA/tracks.conf
cat $DATA_DIR/cv11/sRNASeq_mock_avRPM_strand-.bw.conf       >> $JBROWSE_DATA/tracks.conf
cat $DATA_DIR/cv11/sRNASeq_pool_strand+.bw.conf             >> $JBROWSE_DATA/tracks.conf
cat $DATA_DIR/cv11/sRNASeq_pool_strand-.bw.conf             >> $JBROWSE_DATA/tracks.conf
cat $DATA_DIR/cv11/bidirectional_WTSS.bw.conf               >> $JBROWSE_DATA/tracks.conf

generate-names.pl --safeMode -v --out $JBROWSE_DATA
