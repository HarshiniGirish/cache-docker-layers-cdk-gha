FROM lambci/lambda:build-python3.8 AS build

WORKDIR /tmp

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt -t /asset

COPY handler.py /asset/handler.py

CMD [ "echo", "ready to go!" ]

# Discard everything but the asset directory
FROM scratch as asset

COPY --from=build /asset /asset