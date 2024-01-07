FROM python:3

ARG LIB_DIR=/app/lib
COPY /src/python $LIB_DIR/src/python

COPY /src/python/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR $LIB_DIR/src/python

CMD [ "python", "./app.py" ]
