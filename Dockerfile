# set a base image: https://hub.docker.com/_/python?tab=tags&page=1&ordering=last_updated
FROM python:3.8

# optional: ensure that pip is up to date
RUN pip install --upgrade pip

# first we COPY only requirements.txt to ensure that later builds
# with changes to your src code will be faster due to caching of this layer
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy all your custom modules and files from the src directory
COPY src/ .

# specify the script that will be executed on container start
CMD [ "python", "etl.py"]