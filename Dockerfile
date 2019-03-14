FROM dockerproxy.bale.ai/python:3.7

WORKDIR /bot_root

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY ./ ./
CMD ["python", "customer_bot/main.py"]
#CMD ["python", "seller_bot/main.py"]
ENV PYTHONPATH /bot_root
