# Simple Flask APP Template

### Build docker image
```bash
docker build -t simple-flask -f Dockerfile .
```

### Run docker container
```bash
docker run -d -p 5000:5000 simple-flask
```