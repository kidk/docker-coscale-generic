FROM python:2.7

COPY . /root/

CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"
