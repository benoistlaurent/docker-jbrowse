
help:
	@echo "usage: make <command>"
	@echo ""
	@echo "Available commands:"
	@echo "    help - show this help message"
	@echo "    build - build docker container"
	@echo "    run - start the JBrowse server"
	@echo "    kill - kill the JBrowse server"

build:
	docker build -t jbrowse:1.12.0 .

run: run-cv11

run-batch:
	docker run -it --rm --name jb -p 8080:80 -v `pwd`/$(DATA):/data jbrowse:1.12.0 bash

kill:
	docker kill jb

# .PHONY: data
# data:
# 	JBROWSE_DATA=jbrowse_data DATA_DIR=data source data/load.sh

run-volvox:
	docker run --rm --name jb -p 8080:80 -v `pwd`/data/volvox:/data jbrowse:1.12.0

run-youpi:
	docker run --rm --name jb -p 8080:80 -v `pwd`/data/youpi:/data jbrowse:1.12.0

run-cv11:
	docker run --rm --name jb -p 8080:80 -v `pwd`/data/cv11:/data jbrowse:1.12.0