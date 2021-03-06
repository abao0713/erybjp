FROM python:3.8.6

RUN mkdir -p /usr/src/app/erybjp

WORKDIR /usr/src/app/erybjp

RUN rm -rf /usr/src/app/erybjp

COPY . /usr/src/app/erybjp


RUN pip3 install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

EXPOSE 6851
