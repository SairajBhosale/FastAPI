# Base Image
FROM python:3.9

# workdir
WORKDIR /fastapp

# Copy requirements file
COPY . . 

# run
RUN pip install -r requirements.txt

# port
EXPOSE 8000

# command
CMD ["uvicorn", "fastapp:app", "--host", "0.0.0.0", "--port", "8000"]


