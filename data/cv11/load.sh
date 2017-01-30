#!/bin/bash

rm -rf $JBROWSE_DATA/*

mkdir -p $JBROWSE_DATA/raw/
ln -s $DATA_DIR/cv11/ $JBROWSE_DATA/raw/cv11
ln -sf $DATA_DIR/cv11.json $JBROWSE_DATA/raw/

prepare-refseqs.pl --fasta $DATA_DIR/cv11/cv11.fa --out $JBROWSE_DATA
biodb-to-json.pl -v --conf $DATA_DIR/cv11.json --out $JBROWSE_DATA

#cat $DATA_DIR/cv11/cv11.gff3.conf                >> $JBROWSE_DATA/tracks.conf

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
