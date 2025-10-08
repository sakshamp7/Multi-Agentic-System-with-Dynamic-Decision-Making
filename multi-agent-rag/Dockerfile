FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip && pip install -r backend/requirements.txt
ENV FLASK_APP=backend/app.py
EXPOSE 7860
CMD ["gunicorn","-w","2","-b","0.0.0.0:7860","backend.app:create_app()"]
