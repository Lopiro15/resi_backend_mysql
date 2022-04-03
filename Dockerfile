#On installe tout les packages nécessaires
FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY . /code

RUN pip install -r requirements.txt 

ENV SPIDER=/code

# RUN apt-get update && apt-get install -y \
#     git \
#     python3 \
#     python3-pip \
#     mysql-server \
#     libmysqlclient-dev \
#     supervisor \
#     nginx

# #On installe les dépendances nécessaires au projet et on copie dans /code
# RUN mkdir /code
# WORKDIR /code
# COPY requirements.txt /code/
# RUN pip install -r requirements.txt 
 
# COPY . /code/