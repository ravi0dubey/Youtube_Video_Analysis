import requests
import json
from googleapiclient.discovery import  build

class YTstats:

    def __init__(self,api_key,channel_id):
        self.api_key= api_key
        self.channel_id = channel_id
        self.channel_statistics = None


    def get_channel_statistics(self):
        self.all_data = []
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.request = self.youtube.channels().list(part='snippet,contentDetails,statistics',id=','.join(self.channel_id))
        self.response = self.request.execute()

        for i in range(len(self.response['items'])):
            data = dict(Channel_name=self.response['items'][i]['snippet']['title'],
                        Subscribers=self.response['items'][i]['statistics']['subscriberCount'],
                        Views=self.response['items'][i]['statistics']['viewCount'],
                        Total_Videos=self.response['items'][i]['statistics']['videoCount'],
                        playlist_ID=self.response['items'][i]['contentDetails']['relatedPlaylists']['uploads'])
            self.all_data.append(data)

        return self.all_data

# function to get videosid

    def get_videos_id(self,playlist_ID):
        self.request1= self.youtube.playlistItems().list(part='contentDetails',playlistId=playlist_ID, maxResults=50)
        self.response1=self.request1.execute()
        video_ids = []

        for i in range(len(self.response1['items'])):
            video_ids.append(self.response1['items'][i]['contentDetails']['videoId'])

        self.next_page_token = self.response1.get('nextPageToken')
        self.more_pages = True

        while self.more_pages:
            if self.next_page_token  is None:
                self.more_pages = False
            else:
                self.request2 = self.youtube.playlistItems().list(
                    part='contentDetails',
                    playlistId=playlist_ID,
                    maxResults=50,
                    pageToken=self.next_page_token)
                self.response2 = self.request2.execute()

            for i in range(len(self.response2['items'])):
                video_ids.append(self.response2['items'][i]['contentDetails']['videoId'])

            next_page_token = self.response2.get('nextPageToken')

        return video_ids


## Function to get video details

    def get_video_details(self, video_ids):
        all_video_stats = []

        for i in range(0, len(video_ids), 50):
            request = self.youtube.videos().list(
                part='snippet,statistics',
                id=','.join(video_ids[i:i + 50]))
            response = request.execute()

            for video in response['items']:
                video_stats = dict(Title=video['snippet']['title'],
                                   Published_date=video['snippet']['publishedAt'],
                                   Views=video['statistics']['viewCount'],
                                   Likes=video['statistics']['likeCount'],
                                   Dislikes=video['statistics']['dislikeCount'],
                                   Comments=video['statistics']['commentCount']
                                   )
                all_video_stats.append(video_stats)

        return all_video_stats