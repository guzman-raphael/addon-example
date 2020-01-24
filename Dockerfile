FROM python:3.7-alpine3.10

RUN \
    # for packaging to PyPi (last one for signing with gpg)
    apk add gcc musl-dev libffi-dev openssl-dev && \
    pip install --user twine && \
    # for manual signing dev (necessary)
    apk add openssl git