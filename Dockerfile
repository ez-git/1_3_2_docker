FROM python:3.9
WORKDIR .
COPY . .
RUN pip install -r requirements.txt
RUN python manage.py migrate

EXPOSE 8882

CMD ["python", "./manage.py", "runserver", "0.0.0.0:80"]

