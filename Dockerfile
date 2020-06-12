FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /cook_shop
WORKDIR /cook_shop
ADD requirements.txt /cook_shop/
RUN pip install -r requirements.txt
ADD . /cook_shop/
