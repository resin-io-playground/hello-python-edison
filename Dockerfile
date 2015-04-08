FROM resin/i386-debian:latest

# Install Python.
RUN apt-get update && apt-get install -y python

ADD . /app

CMD ["python", "/app/hello.py"]
