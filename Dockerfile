FROM python:3.10.12
LABEL maintainer="madilat@gmail.com"
USER root
WORKDIR /app
ADD . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 80
ENV NAME World
CMD ["python", "app.py"]