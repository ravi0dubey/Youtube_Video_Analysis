import requests
import json
from googleapiclient.discovery import  build

class YTstats:

    def __init__(self,api_key,channel_id):
        self.api_key= api_key
        self.channel_id = channel_id
        self.channel_statistics = None


    def get_channel_statistics(self):
        all_data = []
        youtube = build('youtube', 'v3', developerKey=self.api_key)
        print(self.channel_id)
        request = youtube.channels().list(part='snippet,contentDetails,statistics',id=','.join(self.channel_id))
        response = request.execute()
        for i in range(len(response['items'])):
            data = dict(Channel_name=response['items'][i]['snippet']['title'],
                        Subscribers=response['items'][i]['statistics']['subscriberCount'],
                        Views=response['items'][i]['statistics']['viewCount'],
                        Total_videos=response['items'][i]['statistics']['videoCount'],
                        playlist_id=response['items'][i]['contentDetails']['relatedPlaylists']['uploads'])
            all_data.append(data)

        return all_data