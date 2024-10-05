FROM python
EXPOSE 5000:5000
EXPOSE 5001:5001
WORKDIR /usr/myapp/
COPY . .
WORKDIR /usr/myapp/
RUN pip install -r requirements.txt
CMD python -m flask run