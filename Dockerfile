FROM python:3.9-alpine
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./ /code/app
VOLUME /app/uploads
CMD ["fastapi", "run", "app/app.py", "--port", "80"]