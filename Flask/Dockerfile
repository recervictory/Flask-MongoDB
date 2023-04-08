FROM python:3.6-alpine
ADD . /app
WORKDIR /app
EXPOSE 5000
RUN pip install -r requirements.txt
ENV PORT=5000 FLASK_DEBUG=1 HOST=mongodb
CMD ["python", "app.py"]