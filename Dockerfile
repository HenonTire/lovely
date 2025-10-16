# Use official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Ensure /app is writable
RUN chmod 777 /app

# Copy requirements and install
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# Copy project files
COPY . /app/

# Expose Django port
EXPOSE 8000

# Run Django server
CMD ["gunicorn", "lovely.wsgi:application", "--bind", "0.0.0.0:8000"]
# docker run --rm -e SECRET_KEY='django-insecure-4)95oan_0c73yt*@5vi-lg1h0+h^h!3vb#myfscfj)452gj@+4' -e DEBUG='False' -e DATABASE_URL='postgresql://postgres:qaQZtCgLmir3BZng@db.ewjzfnlpfunartffyrdf.supabase.co:5432/postgres' lovely-app python manage.py migrate
