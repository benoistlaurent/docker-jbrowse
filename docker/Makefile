
DATA = ../data/cv11

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

run:
	docker run --rm --name jb -p 8080:80 -v `pwd`/$(DATA):/data jbrowse:1.12.0

run-batch:
	docker run -it --rm --name jb -p 8080:80 -v `pwd`/$(DATA):/data jbrowse:1.12.0 bash

kill:
	docker kill jb
