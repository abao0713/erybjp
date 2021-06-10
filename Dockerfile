FROM python:3.8.6

RUN mkdir -p /usr/src/app/erybjp

WORKDIR /usr/src/app/erybjp

RUN rm -rf /usr/src/app/erybjp

COPY . /usr/src/app/erybjp


RUN wget --no-cache https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm && \
yum install google-chrome-stable_current_x86_64.rpm && pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

EXPOSE 6851

CMD [ "uwsgi","--ini","./uwsgi.ini"]

