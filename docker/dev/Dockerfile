FROM surasakp/todobackend-base:latest
MAINTAINER surasakp <bell.sph@gmail.com>

# Install dev/build dependencies
RUN apt-get update && \
    apt-get install -qy python-dev libpq-dev

# Activate virtual environment and install wheel support
RUN . /appenv/bin/activate

# PIP environment variables (NOTE: must be set after installing wheel)
ENV XDG_CACHE_HOME=/cache

# OUTPUT: Test reports are output here
VOLUME /reports

# Add test entrypoint script
COPY scripts/test.sh /usr/local/bin/test.sh
RUN chmod +x /usr/local/bin/test.sh

# Set defaults for entrypoint and command string
ENTRYPOINT ["test.sh"]
CMD ["python", "manage.py", "test", "--noinput"]

# Add application source
COPY src /application
WORKDIR /application

