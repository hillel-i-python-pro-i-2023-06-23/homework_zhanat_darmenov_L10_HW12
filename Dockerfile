FROM python:3.11

ENV PYTHONUNBUFFERED=1

ARG WORKDIR=/wd
ARG USER=user

WORKDIR ${WORKDIR}

RUN useradd --system ${USER} && \
    chown --recursive ${USER} ${WORKDIR}

RUN apt update && apt upgrade -y
RUN apt install -y curl

COPY --chown=${USER} requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install --requirement requirements.txt

COPY --chown=${USER} ./manage.py manage.py
COPY --chown=${USER} ./templates templates
COPY --chown=${USER} ./first_app first_app
COPY --chown=${USER} ./homework_10_2_zhanat_darmenov homework_10_2_zhanat_darmenov

USER ${USER}

VOLUME ${WORKDIR}/db

EXPOSE 8000

ENTRYPOINT ["python", "manage.py", "runserver"]
