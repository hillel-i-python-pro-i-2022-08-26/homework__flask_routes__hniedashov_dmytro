FROM python:3.10

ENV PYTHONUNBUFFERED=1

ARG WORKDIR=/api
ARG USER=api

WORKDIR ${WORKDIR}

RUN useradd --system ${USER}
RUN chown ${USER} ${WORKDIR}

COPY --chown=${USER} requirements.txt requirements.txt
COPY --chown=${USER} app.py app.py

RUN pip install --upgrade pip && \
    pip install --requirement requirements.txt

USER ${USER}
