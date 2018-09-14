FROM surasakp/todobackend-base:latest
MAINTAINER surasakp <bell.sph@gmail.com>

# Copy application
COPY /src/ /application

# Activate virtual environment
WORKDIR /application

# Install application
RUN . /appenv/bin/activate && \
    pip install . && \
    pip install -r requirements.txt && \
    pip install uwsgi
