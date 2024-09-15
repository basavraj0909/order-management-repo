FROM python:3.9

ENV PYTHONUNBUFFERED=1

# Set the working directory

WORKDIR /code

COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

COPY . .

# Expose the Django default port
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

