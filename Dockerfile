#On installe tout les packages nécessaires
FROM ubuntu:latest
RUN apt-get update && apt-get install -y \
    git \
    python3 \
    python3-pip 

#On installe les dépendances nécessaires au projet et on copie dans /code
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt 
 
COPY . /code/