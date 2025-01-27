import requests

import time
from datetime import datetime

# Get the current time in seconds since the Unix epoch
current_time_seconds = time.time()

# Convert to a readable date and time format
readable_time = datetime.fromtimestamp(current_time_seconds).strftime('%d-%m-%Y %H:%M:%S')

url = "https://nnr-backend-3c6q.onrender.com/"
# payload = {"Scheduled": "CRON SCHEDULED", "time": readable_time}  # Adjust payload as needed
headers = {"Content-Type": "application/json"}

response = requests.get(url)
print(f"Status Code: {response.status_code}, Response: {response.text}")