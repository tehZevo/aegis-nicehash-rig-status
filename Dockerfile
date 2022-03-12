FROM python:3.7

WORKDIR /app

RUN apt-get install git -y
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 80

CMD [ "python", "-u", "main.py" ]
