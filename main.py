import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from Youtube_Statstistic import YTstats

api_key = 'AIzaSyCIQem_fJ-mTWtZnbQufdlGytz9Qqav16Y'
channel_ids = ['UCnz-ZXXER4jOvuED5trXfEA', # techTFQ
               'UCLLw7jmFsvfIVaUFsLs8mlQ', # Luke Barousse
               'UCiT9RITQ9PW6BhXK0y2jaeg', # Ken Jee
               'UC7cs8q-gJRlGwj4A8OmCmXg', # Alex the analyst
               'UC2UXDak6o7rBm23k3Vv5dww' # Tina Huang
              ]

yt= YTstats(api_key,channel_ids )
channel_statistics = yt.get_channel_statistics()
channel_data = pd.DataFrame(channel_statistics)
channel_data['Subscribers']= pd.to_numeric(channel_data['Subscribers'])
channel_data['Views']= pd.to_numeric(channel_data['Views'])
channel_data['Total_Videos']= pd.to_numeric(channel_data['Total_Videos'])


# ax_subscribers_count= sns.barplot(x='Channel_name',y='Subscribers',data= channel_data)
# # plt.show()
# ax_views_count = sns.barplot(x='Channel_name',y='Views',data= channel_data)
# # plt.show()
# ax_views_count = sns.barplot(x='Channel_name',y='Total_Videos',data= channel_data)
# # plt.show()
#
#get playlist id of particular User
playlist_id = channel_data.loc[channel_data['Channel_name']=='Ken Jee','playlist_ID'].iloc[0]

#get all Videos_id of the Particular User
videos_id = yt.get_videos_id(playlist_id)
print(videos_id)

# # Get all videos details of Particular User
# video_details = yt.get_video_details(videos_id)
# video_data = pd.DataFrame(video_details)
#
# video_data['Published_date'] = pd.to_datetime(video_data['Published_date']).dt.date
# video_data['Views'] = pd.to_numeric(video_data['Views'])
# video_data['Likes'] = pd.to_numeric(video_data['Likes'])
# # video_data['Dislikes'] = pd.to_numeric(video_data['Dislikes'])
# video_data['Views'] = pd.to_numeric(video_data['Views'])
# video_data['Month'] = pd.to_datetime(video_data['Published_date']).dt.strftime('%b')
# top10_videos = video_data.sort_values(by='Views', ascending=False).head(10)
# print(top10_videos)
#
# ax_top_10_videos = sns.barplot(x='Views', y='Title', data=top10_videos)
# plt.show()
#
# videos_per_month = video_data.groupby('Month', as_index=False).size()
# sort_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# videos_per_month.index = pd.CategoricalIndex(videos_per_month['Month'], categories=sort_order, ordered=True)
# videos_per_month = videos_per_month.sort_index()
# ax_permonth_videso = sns.barplot(x='Month', y='size', data=videos_per_month)
# plt.show()

#to get each videos Comments
# video_comments_details = yt.get_video_comments(videos_id)
video_comments_details = yt.get_video_comments()
print(video_comments_details)




