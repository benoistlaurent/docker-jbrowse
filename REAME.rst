
JBrowse-cv11
************

This package contains the material to setup a JBrowser instance for
the Chlamydomonas genome.


Pre-requisite: install JBrowse
==============================

Docker
------

Using the docker image consist in two main steps, namely

- building the docker image
- running the a docker container of the image

Here is the full procedure:

    .. code-block:: bash

        $ cd docker
        $ docker build -t jbrowse:1.12.0 .
        $ docker run --rm --name jb -p 8080:80 -v `pwd`/../data/cv11:/data jbrowse:1.12.0

Alternatively, one can use the Makefile present in the docker directory:

    .. code-block:: bash

        $ cd docker
        $ make build
        $ make run


System
------

The installation instructions to install the JBrowse instance on a system
in based on the docker image construction instruction (see `docker/Dockerfile`).

1. Install system dependancies:

    .. code-block:: bash

        $ sudo apt-get update && sudo apt-get install -yqq build-essential\
            apache2\
            git\
            libexpat-dev\
            libpq-dev\
            libpng12-dev\
            libxml2-dev\
            postgresql-client\
            unzip\
            wget\
            zlib1g-dev

2. Download and install JBrowse:

    .. code-block:: bash

        $ # Clone JBrowse repository and update to tag 1.12.0-release
        $ git clone --recursive --branch 1.12.0-release https://github.com/gmod/jbrowse jbrowse-1.12.0
        $ # Install dependencies
        $ cd jbrowse-1.12.0
        $ sudo ./bin/cpanm --force\
            Devel::Size\
            DBD::SQLite\
            Digest::Crc32\
            Exception::Class\
            File::Next\
            File::Copy::Recursive\
            Hash::Merge\
            Heap::Simple\
            Heap::Simple::XS\
            JSON\
            JSON::XS\
            List::MoreUtils\
            local::lib\
            Parse::RecDescent\
            PerlIO::gzip\
            Test::Warn\
            Bio::Perl\
            Bio::FeatureIO\
            Bio::GFF3::LowLevel::Parser\
            Bio::SeqFeature::Annotated\
            Bio::DB::SeqFeature::Store\
            Bio::DB::Das::Chado && \
            ./setup.sh
        $ # Build and install JBrowse itself
        $ perl Makefile.PL && make && sudo make install
        $ sudo rm -r /var/www/html && sudo ln -s $HOME/jbrowse-1.12.0 /var/www/html


Install Chlamydomonas data and setup JBrowse
============================================

Installing and setting-up cv11 data consist in two steps:

1. Setup environment variables:
   
    .. code-block:: bash

        $ echo "export JBROWSE=$HOME/jbrowse-1.12.0" > $HOME/.jbrowserc
        $ echo "export JBROWSE_DATA=\$JBROWSE/data"  >> $HOME/.jbrowserc
        $ echo "export CV11_REPO=$HOME/jbrowse-cv11" >> $HOME/.jbrowserc
        $ echo "export CV11_DATA_DIR=\$CV11_REPO/data" >> $HOME/.jbrowserc
        $ # Add this line to $HOME/.profile so that jbrowserc is sourced at each login.
        $ echo '[ -f "$HOME/.jbrowserc" ] && . $HOME/.jbrowserc' >> $HOME/.profile
        $ . $HOME/.jbrowserc

2. Download the cv11 data repository:
   
    .. code-block:: bash

        $ git clone https://github.com/benoistlaurent/jbrowse-cv11.git $CV11_REPO

- Setup JBrowse instance (copy files at appropriate places and run JBrowse setup scripts):

    .. code-block:: bash

        $ cd $CV11_REPO
        $ bash install.bash


Update data
===========

To update data from an existing JBrowse instance, the procedure is the same
as for installation:

    .. code-block:: bash

        $ cd $CV11_REPO
        $ bash install.bash
