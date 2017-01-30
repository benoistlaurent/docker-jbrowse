# This is a Dockerfile for JBrowse.

FROM nginx
MAINTAINER Benoist LAURENT <benoist.laurent@ibpc.fr>

ENV JBROWSE_VERSION 1.12.0
ENV JBROWSE_VERSION_TAG ${JBROWSE_VERSION}-release

RUN apt-get -qq update --fix-missing && \
    DEBIAN_FRONTEND=noninteractive apt-get install -yqq\
        build-essential\
        git\
        libexpat-dev\
        libpq-dev\
        libpng12-dev\
        libxml2-dev\
        postgresql-client\
        unzip\
        wget\
        zlib1g-dev
        

RUN git clone --recursive --branch ${JBROWSE_VERSION_TAG} https://github.com/gmod/jbrowse /jbrowse

WORKDIR /jbrowse/
RUN ./bin/cpanm --force\
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
    ./setup.sh && \
    rm -rf /root/.cpan/

RUN perl Makefile.PL && make && make install
RUN rm -rf /usr/share/nginx/html && ln -s /jbrowse/ /usr/share/nginx/html

VOLUME /data
COPY docker-entrypoint.sh /
CMD ["/docker-entrypoint.sh"]


# # ./setup.sh
# Installing Perl prerequisites ... done.

# Formatting Volvox example data ... done.
# To see the volvox example data, browse to http://your.jbrowse.root/index.html?data=sample_data/json/volvox.

# Formatting Yeast example data ... done.
# To see the yeast example data, browse to http://your.jbrowse.root/index.html?data=sample_data/json/yeast.

# Building and installing legacy wiggle format support (superseded by BigWig tracks) ... done.

# Building and installing legacy bam-to-json.pl support (superseded by direct BAM tracks) ... done.