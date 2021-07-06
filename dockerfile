FROM python:3.7

COPY D:\my_space\end to end\StonePaperScissor /home

WORKDIR /home

ADD . .

RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]
