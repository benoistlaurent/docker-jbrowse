
#
# Install data to JBrowse data directory.
# 
# This Makefile assumes that those environment variables are adequatly set:
#   - JBROWSE_DATA: path to JBrowse data directory
#   - CV11_DATA_DIR: path to the directory where are cv11.json.in and cv11 directory
#

JBROWSE_RAW_DATA_DIR = $(JBROWSE_DATA)/raw

# Input files.
CONF_TRACKS = $(CV11_DATA_DIR)/cv11/directional_WTSS_RPM_strand+.bw.conf \
              $(CV11_DATA_DIR)/cv11/directional_WTSS_RPM_strand-.bw.conf \
              $(CV11_DATA_DIR)/cv11/sRNASeq_RPP_avRPM_strand+.bw.conf \
              $(CV11_DATA_DIR)/cv11/sRNASeq_RPP_avRPM_strand-.bw.conf \
              $(CV11_DATA_DIR)/cv11/sRNASeq_mock_avRPM_strand+.bw.conf \
              $(CV11_DATA_DIR)/cv11/sRNASeq_mock_avRPM_strand-.bw.conf \
              $(CV11_DATA_DIR)/cv11/sRNASeq_pool_strand+.bw.conf \
              $(CV11_DATA_DIR)/cv11/sRNASeq_pool_strand-.bw.conf \
              $(CV11_DATA_DIR)/cv11/bidirectional_WTSS.bw.conf \

INPUT_FASTA = $(CV11_DATA_DIR)/cv11/cv11.fa

# Targets.
JSON = $(JBROWSE_DATA)/raw/cv11.json
RAW_DATA = $(JBROWSE_DATA)/raw/cv11
TRACKS = $(JBROWSE_DATA)/tracks.conf
TARGETS = $(JSON)


all:
	@echo "usage: make <command>"
	@echo ""
	@echo "Available commands:"
	@echo "    install - remove installed files and re-run installation procedure"
	@echo "    clean - remove installed files"


install: $(TRACKS) $(RAW_DATA) $(JSON) trackList.json


trackList.json: $(INPUT_FASTA) $(JSON) $(JBROWSE_DATA)
	prepare-refseqs.pl --fasta $(INPUT_FASTA) --out $(JBROWSE_DATA)
	biodb-to-json.pl -v --conf $(JSON) --out $(JBROWSE_DATA)


$(JSON): $(CV11_DATA_DIR)/cv11.json.in $(JBROWSE_RAW_DATA_DIR)
	sed 's#@DATA_DIR@#'"$(JBROWSE_RAW_DATA_DIR)"'#' $< > $@

$(RAW_DATA): $(JBROWSE_RAW_DATA_DIR)
	cp -r $(CV11_DATA_DIR)/cv11 $@

$(TRACKS): $(JBROWSE_DATA)
	cat $(CONF_TRACKS) > $@


$(JBROWSE_RAW_DATA_DIR): $(JBROWSE_DATA)
	mkdir $@


$(JBROWSE_DATA): $(JBROWSE)
	mkdir $@

clean:
	rm -rf $(JBROWSE_DATA)