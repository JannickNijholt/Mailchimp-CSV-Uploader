import csv
import requests
import os
import json
from datetime import datetime
import sys

# Settings (adjust these as needed)
api_key = "XXXXXXXXX"
audience_id = "XXXXXXXX"
server_prefix = "XXXXX"
csv_file_location = os.path.join(os.path.dirname(os.path.realpath(__file__)), "emails.csv")
current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Create a new folder for the audience id, date and time
folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), f"{audience_id}_{current_datetime}")
os.makedirs(folder_path, exist_ok=True)

# Create file paths for ok.csv and failed.csv within the new folder
ok_file_location = os.path.join(folder_path, "ok.csv")
failed_file_location = os.path.join(folder_path, "failed.csv")

# URL for adding members to a Mailchimp list
url = f"https://{server_prefix}.api.mailchimp.com/3.0/lists/{audience_id}/members"

# Headers for the API request
headers = {
    "Content-Type": "application/json",
    "Authorization": f"apikey {api_key}"
}

# Read the total number of contacts
with open(csv_file_location, "r", encoding="utf-8") as file:
    total_contacts = sum(1 for row in csv.reader(file)) - 1  # -1 for the header

# Read email addresses and full names from a CSV file and add them as a member of the Mailchimp list
with open(csv_file_location, "r", encoding="utf-8") as file, \
     open(ok_file_location, "w", newline='', encoding="utf-8") as ok_file, \
     open(failed_file_location, "w", newline='', encoding="utf-8") as failed_file:
    
    reader = csv.reader(file)
    ok_writer = csv.writer(ok_file)
    failed_writer = csv.writer(failed_file)

    next(reader)  # skip header row
    
    contacts_imported = 0
    contacts_failed = 0

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
            ok_writer.writerow([first_name, last_name, email])
            contacts_imported += 1
        else:  # Any other status
            failed_writer.writerow([first_name, last_name, email, json.dumps(response_data, indent=2)])
            contacts_failed += 1

        # Display import progress
        contacts_remaining = total_contacts - contacts_imported - contacts_failed
        sys.stdout.write("\rContacts remaining: {0} ({1}%), Imported: {2} ({3}%), Failed: {4} ({5}%)".format(
            contacts_remaining, contacts_remaining / total_contacts * 100,
            contacts_imported, contacts_imported / total_contacts * 100,
            contacts_failed, contacts_failed / total_contacts * 100))
        sys.stdout.flush()
