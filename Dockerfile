FROM tensorflow/tensorflow:latest-gpu

RUN apt-get update
RUN apt-get install -y libgl1-mesa-dev
RUN pip install keras numpy pillow flask

COPY . .

EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["server.py"]
