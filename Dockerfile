FROM python:3.8-alpine

RUN adduser -D myblog

WORKDIR /home/myblog

COPY requirements.txt requirements.txt
RUN python -m venv myenv
RUN myenv/bin/pip install -r requirements.txt
RUN myenv/bin/pip install gunicorn pymysql

COPY app app
COPY migrations migrations
COPY myblog.py config.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP myblog.py

RUN chown -R myblog:myblog ./
USER myblog

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
