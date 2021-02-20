FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
RUN curl -sL https://deb.nodesource.com/setup_15.x | bash -
RUN apt-get install -y nodejs
COPY requirements.txt /code/
COPY package*.json /code/
RUN pip install -r requirements.txt
RUN npm install
COPY . /code/
RUN ["chmod", "+x", "/code/docker-entrypoint.sh"]
WORKDIR /code/client
RUN npm run build
WORKDIR /code
