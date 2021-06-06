FROM python:3.8.6

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

RUN rm -rf /usr/src/app

COPY . /usr/src/app

RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt


#CMD [ "uwsgi", "./uwsgi.ini"]

