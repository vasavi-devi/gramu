FROM python: 3.9

WORKDIR /app

COPY requirement.txt .

RUN pip install -r requrement.txt

COPY . .

EXPOSE 50000

CMD ["python"  "app.py"]
