
from googleapiclient.discovery import build

def get_channel_id(api_key, username):
    youtube = build('youtube', 'v3', developerKey=api_key)
    response = youtube.channels().list(part='snippet', forUsername=username).execute()
    
    try:
        channel_id = response['items'][0]['id']
        return channel_id
    except KeyError:
        print(f"Channel ID for username '{username}' not found.")
        return None

api_key = 'AIzaSyBTgO4S_p3UAGYhGzz5qDuGj6YAUHvSwgE'
username = 'vogue'

channel_id = get_channel_id(api_key, username)
if channel_id:
    print("Channel ID:", channel_id)
