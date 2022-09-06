import pandas as pd
import seaborn as sns


from Youtube_Statstistic import YTstats
api_key = 'AIzaSyCIQem_fJ-mTWtZnbQufdlGytz9Qqav16Y'
channel_ids = ['UCnz-ZXXER4jOvuED5trXfEA', # techTFQ
               'UCLLw7jmFsvfIVaUFsLs8mlQ', # Luke Barousse
               'UCiT9RITQ9PW6BhXK0y2jaeg', # Ken Jee
               'UC7cs8q-gJRlGwj4A8OmCmXg', # Alex the analyst
               'UC2UXDak6o7rBm23k3Vv5dww' # Tina Huang
              ]


yt= YTstats(api_key,channel_ids )
channel_Statistics = yt.get_channel_statistics()
print(channel_Statistics)

