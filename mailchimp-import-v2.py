import csv
import requests
import os
import json
from datetime import datetime

# Settings
api_key = "xxxxxxxxxxxxxxxxxxxxxxx-xxxxx"
audience_id = "xxxxxxxxxxxx"
server_prefix = "xxxxx"
csv_file_location = os.path.join(os.path.dirname(os.path.realpath(__file__)), "emails.csv")
current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file_location = os.path.join(os.path.dirname(os.path.realpath(__file__)), f"mailchimp-import-log_{audience_id}_{current_datetime}.txt")

# URL to add subscribers to the Mailchimp audience
url = f"https://{server_prefix}.api.mailchimp.com/3.0/lists/{audience_id}/members"

# Headers for the API-request
headers = {
    "Content-Type": "application/json",
    "Authorization": f"apikey {api_key}"
}

# Read emaialdressses and the full name from the CSV-file and add them as a subscriber to the Mailchimp audience.
with open(csv_file_location, "r", encoding="utf-8") as file, open(log_file_location, "a") as log_file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        first_name, last_name, email = row
        data = {
            "email_address": email,
            "status": "subscribed",
            "merge_fields": {
                "FNAME": first_name,
                "LNAME": last_name
            }
        }
        response = requests.post(url, headers=headers, json=data)
        response_data = json.loads(response.text)

        if response.status_code == 200:  # Successful subscription
            log_message = f"{email} - {response_data['status']}\n"
        else:  # Any other status
            log_message = json.dumps(response_data, indent=2) + "\n"

        log_file.write(log_message)
