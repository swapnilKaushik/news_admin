# BASE image
FROM python:3.10-slim

ARG django_settings_module=news_admin.settings

# ----- A GREEN_ENV="happy environment" -----
# PYTHON:
# 1. Do not buffer the output stream
# 2. Do not generate *.pyc files
# 3. Set timezone to UTC
# 4. Select the settings file to be used
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV TZ=UTC
ENV DJANGO_SETTINGS_MODULE=${django_settings_module}
ENV PYTHONFAULTHANDLER=1
# PIP:
ENV PIP_NO_CACHE_DIR=off 
ENV PIP_DISABLE_PIP_VERSION_CHECK=on 
ENV PIP_DEFAULT_TIMEOUT=100


# Install vital elements
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    gdal-bin \
    libgdal-dev \
    && pip install --upgrade pip \
    && pip install gunicorn


# Construct the cockpit
RUN mkdir /code
# set work directory
WORKDIR /code


# Install app vital elements
COPY news_admin/requirements.txt .
RUN pip install -r requirements.txt