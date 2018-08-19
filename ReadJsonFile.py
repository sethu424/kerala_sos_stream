'''
Created on 19-Aug-2018

@author: sethu
'''

import json

if __name__ == '__main__':
    with open("/Users/sethu/Documents/temp.json") as fp:
        json_data = json.load(fp)
        
        tweet_text = json_data["text"]
        print("tweet:", tweet_text)
        e_tweet_text = json_data["retweeted_status"]["extended_tweet"]["full_text"]
        print("extended tweet:", e_tweet_text)