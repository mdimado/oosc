FROM gcr.io/oss-fuzz-base/base-builder-python

RUN git clone https://github.com/trentm/python-markdown2 markdown2

COPY *.sh *py $SRC/

WORKDIR $SRC/markdown2


