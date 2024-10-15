FROM python
EXPOSE 30331:30331
EXPOSE 30333:30333
WORKDIR /usr/myapp/
COPY . .
WORKDIR /usr/myapp/
RUN pip install -r requirements.txt
ENV ENV="local"
CMD ["python", "app.py"]