FROM python
MAINTAINER Michael Mortenson
ADD . /python-app/flask_app_for_Jenkins
WORKDIR /python-app/flask_app_for_Jenkins
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
