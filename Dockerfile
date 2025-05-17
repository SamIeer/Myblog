FROM python:slim

WORKDIR /#PROJECTS/app

COPY requirements.txt ./
COPY . .

RUN pip install -r requirements.txt
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		sqlite3 \
	&& rm -rf /var/lib/apt/lists/*

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]