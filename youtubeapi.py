import os
from googleapiclient.discovery import build

api_key = os.environ.get("YAPIKEY")
youtube = build('youtube', 'v3', developerKey=api_key)


response = request.execute()

print(response)

