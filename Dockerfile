FROM python:2.7

COPY . /root/

CMD ["python","/felt/main.py","/srv"]

CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"
