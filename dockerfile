FROM python:3.10.8-bullseye

WORKDIR /app

# RUN apt-get update && apt-get install -y \
#     zip \
#     tree \
#     vim \
#     unzip \
#     git \
#     crul

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

USER root

EXPOSE 8080

ENTRYPOINT [ "python" ]

CMD ["app.py"]