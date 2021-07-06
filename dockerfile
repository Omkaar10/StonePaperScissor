FROM python:3.7

COPY . /home

WORKDIR /home

ADD . .

RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]
