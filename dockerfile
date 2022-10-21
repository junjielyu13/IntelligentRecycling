FROM 3.10.8-alpine3.15

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt


COPY . .

CMD ["python3", "-m" , "flask", "run", "-host=0.0.0.0"]