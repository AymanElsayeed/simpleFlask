FROM python
WORKDIR /usr/myapp/
COPY . .
WORKDIR /usr/myapp/
RUN pip install -r requirements.txt
CMD python -m flask run