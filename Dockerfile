FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
RUN curl -sL https://deb.nodesource.com/setup_15.x | bash -
RUN apt-get install -y nodejs
COPY . /code/

# Python deps
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Node deps and build
WORKDIR /code/client
RUN npm install -g npm@7.6.0
RUN npm install
RUN npm run build

WORKDIR /code
RUN ["chmod", "+x", "/code/entrypoint-web.sh"]
RUN ["chmod", "+x", "/code/entrypoint-celery-beat.sh"]
RUN ["chmod", "+x", "/code/entrypoint-celery-worker.sh"]
