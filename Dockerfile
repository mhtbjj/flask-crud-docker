FROM python:3.8.7
ARG portno=5002
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE $portno
ENTRYPOINT ["python"]
CMD ["app.py"]
