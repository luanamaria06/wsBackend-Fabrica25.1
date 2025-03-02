FROM python:3.11-slim


WORKDIR /movies

COPY requirements.txt /movies//

RUN pip install --no-cache-dir -r requirements.txt

COPY . /movies/

EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
