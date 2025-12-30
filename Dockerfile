# Base Image: python 3.12
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# copy source code
COPY src/ ./src
COPY models/ ./models/

# expose port
EXPOSE 8501
EXPOSE 8000

# main command
COPY run_app.sh .
RUN chmod +x run_app.sh

CMD [ "./run_app.sh" ]