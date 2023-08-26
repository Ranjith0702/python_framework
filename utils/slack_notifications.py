import os
import requests
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


# #slack_token = os.getenv('SLACK_TOKEN')
# client = WebClient(token="xoxb-5786642955568-5749504202295-x3jHIhWVjhHSiKaSxgmlHFxL")
#
#
# allure_report_path = 'package-lock.json'
#
#
# def send_slack_notification_with_attachment():
#     try:
#         response = client.files_upload(
#             channels='#projectone',
#             file=allure_report_path,
#             title='Allure Test Report',
#             initial_comment='Here is the latest Allure test report.'
#         )
#         print("Slack notification sent successfully!")
#     except SlackApiError as e:
#         print("Error sending Slack notification:", e.response['error'])
#
#
# send_slack_notification_with_attachment()

import os
import zipfile

import requests
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# slack_token = os.getenv('SLACK_TOKEN')
client = WebClient(token="xoxb-5786642955568-5783697018757-qna9azrGRhrLXAZWVzTEhUj5")

# allure_report_path = "reports\\allure_result"
# Path to the directory you want to send
DIRECTORY_PATH = "C:\\Users\\dell\\Downloads\\Python-Framework-main\\reports"


# Create a zip archive of the directory
def create_zip(directory_path):
    zip_filename = "directory.zip"
    with zipfile.ZipFile(zip_filename, "w") as zipf:
        for foldername, subfolders, filenames in os.walk(directory_path):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                arcname = os.path.relpath(file_path, directory_path)
                zipf.write(file_path, arcname)

    return zip_filename


# Create a zip archive of the directory
zip_filename = create_zip(DIRECTORY_PATH)


def send_slack_notification_with_attachment():
    try:
        response = client.files_upload(
            channels='#projectone',
            file=zip_filename,
            title='Allure Test Report',
            initial_comment='Here is the latest Allure test report.'
        )
        print("Slack notification sent successfully!")
    except SlackApiError as e:
        print("Error sending Slack notification:", e.response['error'])


# Clean up: remove the temporary zip file
os.remove(zip_filename)

create_zip(directory_path="C:\\Users\\dell\\Downloads\\Python-Framework-main\\reports") # path for report directory
send_slack_notification_with_attachment()