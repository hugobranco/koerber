FROM python:3.9-slim

RUN apt-get update && apt-get install -q -y git libpq-dev python3-pip

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt --target=/src/stacking_layers_machine

ENV TZ Europe/Lisbon

ADD ./src       /src/stacking_layers_machine

WORKDIR /src/stacking_layers_machine

CMD ["python", "main.py"]
