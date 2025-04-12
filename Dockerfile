FROM python:3.9-alpine
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY ./ /app
VOLUME /app/uploads
RUN mkdir -p /app/uploads
CMD ["fastapi", "run", "app.py", "--port", "80"]