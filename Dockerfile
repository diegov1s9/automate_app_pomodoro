# Use a Python base image
FROM python:3.12.3

# Set working directory
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Command to run the tests and generate an HTML report
CMD ["python", "-m", "pytest", "-s", "-v", "--html=reports/report.html", "test_app_pomodoro.py::TestAppPomodoro"]
