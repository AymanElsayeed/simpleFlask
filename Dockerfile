FROM python
EXPOSE 30331:30331
EXPOSE 30333:30333
WORKDIR /usr/myapp/
COPY . .
WORKDIR /usr/myapp/
RUN pip install -r requirements.txt
ENV ENV="local"
#ENV FLASK_EXT_PORT=30333
#ENV HOST="0.0.0.0"
CMD ["python", "app.py"]