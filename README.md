# Mailchimp CSV uploader

This Python script imports contacts from a CSV file into a Mailchimp contact list.

## Files

- **emails.csv**: This file contains three fields: First Name (FNAME), Last Name (LNAME), and Email Address. It is crucial to maintain the existing format. This file should include all contacts you wish to import, specifying their first name, last name, and email address.

- **ok.csv and failed.csv**: These files will hold the details of the import process. Each time the script is run, it generates these new files in a new folder named with the Audience ID and timestamp to avoid overwriting previous data. `ok.csv` includes all contacts that have been successfully imported. `failed.csv` includes all contacts that failed to import and the API response for why the import failed.

- **mailchimp-import-v2.py**: This is the Python script that imports contacts from the emails.csv file into a Mailchimp contacts list. Here are the settings you may need to change:
  - **api_key**: Input the API key of the Mailchimp environment where your contacts list is located.
  - **audience_id**: Input the Audience ID of your contacts list. You can find this in the settings of a contacts list.
  - **server_prefix**: Input the server where the Mailchimp environment for your contacts list is hosted. You can find this in the URL bar. For example, if the URL is https://us19.mailchimp.com, the server_prefix is 'us19'.

## How to Use
To use this script, follow these steps:

1. Fill in the emails.csv file with the contacts you want to import. Make sure to format the file correctly, with 'FNAME', 'LNAME', and 'Email Address' fields.
2. Adjust the settings in the mailchimp-import-v2.py script. Input your API key, Audience ID, server prefix as needed.
3. Run the script. Upon successful execution, the contacts from your .csv file will be imported into your Mailchimp contacts list. You can review the import process in the newly created `ok.csv` and `failed.csv` files.

This script will only use fields standard to new Mailchimp audiences to prevent the need for users to create custom fields. It uses the 'FNAME', 'LNAME', and 'Email Address' fields, which should be present in any new Mailchimp audience. If you need to import data in custom fields, you have to edit the script to make sure all other fields in emails.csv are imported succesfully.

Enjoy using the script, and feel free to reach out if you have any questions or suggestions!

