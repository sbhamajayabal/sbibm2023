FROM python:3.6
WORKDIR /sbapp
ADD . /sbapp
COPY requirements.txt /sbapp
RUN python3 -m pip install -r requirements.txt
RUN python3 -m pip ibm_db
EXPOSE 5000
CMD ["python","app.py"]