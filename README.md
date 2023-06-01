# Mailchimp Import Script

Written by: Jannick Nijholt\
Date: 08-05-2023

## Files

- **emails.csv**: This file contains three fields: First Name (FNAME), Last Name (LNAME) and Email Address. It is crucial to maintain the existing format. This file should include all contacts you wish to import, specifying their first name, last name, and email address. 

- **mailchimp-import-log_{audience_id}_{current_datetime}.txt**: This file will hold a log of the import process. Each time the script is run, it generates a new log file with a timestamp to avoid overwriting previous logs. 

- **mailchimp-import-v2.py**: This is the Python script that imports contacts from the emails.csv file into a Mailchimp contacts list. Here are the settings you may need to change:
    - `api_key`: Input the API key of the Mailchimp environment where your contacts list is located.
    - `audience_id`: Input the Audience ID of your contacts list. You can find this in the settings of a contacts list.
    - `server_prefix`: Input the server where the Mailchimp environment for your contacts list is hosted. You can find this in the URL bar. For example, if the URL is https://us19.mailchimp.com, the server_prefix is 'us19'.
    - `csv_file_location`: This is the location of the .csv file. By default, it is set to the same directory as the one from which you are running the Python script.

## How to Use

To use this script, follow these steps:

1. Fill in the emails.csv file with the contacts you want to import. Make sure to format the file correctly, with 'FNAME', 'LNAME', and 'Email Address' fields.
2. Adjust the settings in the mailchimp-import-v2.py script. Input your API key, Audience ID, server prefix, and file locations as needed.
3. Run the script. Upon successful execution, the contacts from your .csv file will be imported into your Mailchimp contacts list. You can review the import log in the newly created log file.

This script will only use fields standard to new Mailchimp audiences to prevent the need for users to create custom fields. It uses the 'FNAME', 'LNAME', and 'Email Address' fields, which should be present in any new Mailchimp audience.

Enjoy using the script, and feel free to reach out if you have any questions or suggestions!
