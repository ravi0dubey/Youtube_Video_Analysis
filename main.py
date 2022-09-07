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
print(channel_data)
# x = channel_data['Channel_name']
# y = channel_data['Subscribers']
# sns.set(rc={'figure.figsize':(10,8)})
ax_subscribers_count= sns.barplot(x='Channel_name',y='Subscribers',data= channel_data)
# plt.bar(x,y)
plt.show()

ax_views_count = sns.barplot(x='Channel_name',y='Views',data= channel_data)
plt.show()

ax_views_count = sns.barplot(x='Channel_name',y='Total_Videos',data= channel_data)
plt.show()

