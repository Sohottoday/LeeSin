FROM python:3.6

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /app
WORKDIR /app
ADD . /app/
ENV PYTHONUNBUFFERED 1

# WORKDIR /usr/src/app
# COPY requirements.txt ./
RUN pip install django==2.1.15
RUN pip install Pillow
RUN pip install beautifulsoup4
RUN pip install requests
RUN pip install django-imagekit==4.0.2
# RUN pip install -r requirements.txt
# COPY . /app/

EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]