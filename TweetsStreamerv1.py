# In[1]:

# Twitter Streaming API using twarc. Code shamelessly taken from 
# - https://labsblog.f-secure.com/2018/01/17/how-to-get-streaming-data-from-twitter/


# In[11]:

import queue
import threading
import sys
import time
import csv
from GoogleSheetsUpdator import GoogleSheetsUpdator

from twarc import Twarc
from googletrans import Translator



# In[9]:

consumer_key="your_consumer_key"
consumer_secret="your_consumer_secret"
access_token="your_access_token"
access_token_secret="your_access_secret"
target_list = ["#keralafloods", "#keralasos"]


# In[10]:

kerala_places=["alappuzha","ambalapuzha","chengannur","cherthala","karthikappally","kuttanad","mavelikkara","kakkanad","aluva","kanayannur","kochi","kothamangalam","kunnathunad","muvattupuzha","paravur","idukki","painavu","devikulam","peerumade","thodupuzha","udumbanchola","kannur","thalassery","thalipparamba","kasaragod","hosdurg","kollam","karunagappally","kottarakkara","kunnathur","pathanapuram","kottayam","changanasserry","kanjirappally","meenachil","vaikom","kozhikode","koyilandy","vadakara","malappuram","eranad","nilambur","perinthalmanna","ponnani","tirur","tirurangadi","palakkad","alathur","chittur","mannarkkad","ottappalam","pathanamthitta","adoor","kozhencherry","mallappally","ranni","thiruvalla","thiruvananthapuram","chirayinkeezhu","nedumangad","neyyattinkara","thrissur","chavakkad","kodungallur","mukundapuram","thalapilly","wayanad","kalpetta","mananthavady","sultanbattery","vythiri","haripad","mankombu","ernakulam","perumbavoor","northparavur","painavu	","peermade","nedumkandam","iritty","payyanur","manjeshwaram","uppala","vellarikundu","chathannoor","sasthamkotta","punalur","palai","thamarassery","vatakara","7taluks[22]","manjeri(eranad)","kondotty","pattambi","konni","hiruvananthapuram","kattakada","attingal","varkala","irinjalakuda","chalakudy","wadakkancheri","kunnamkulam","taliparamba","udma","vallachira","varam","nenmenikkara","paduvilayi","palissery","panniyannur","panoor","pappinisseri","paravoor","pathiriyad","pattiom","payyannur","peralasseri","peringathur","pinarayi","pottore","puranattukara","puthukkad","quilandy","shoranur","narath","kannapuram","kayamkulam","kolazhy","koothuparamba","koratty","kottayam-malabar","manjeshwar","marathakkara","mattannur","mavilayi","mavoor","munderi","kanhangad","kanhirode","kanjikkuzhi","kannadiparamba","bangramanjeshwar","chala","changanassery","chelora","chendamangalam","cheruthazham","chevvoor","chittur","thathamangalam","chockli","erattupetta","guruvayoor","hosabettu","idukkitownship","iriveri","kadirur","kalliasseri","akathiyoor","ancharakandy","arookutty","aroor","avinissery"]

# Creating Google translator 
translator = Translator()

# GoogleSheets Updator
gSheetsUpdator = GoogleSheetsUpdator()

tweets_set = set()


# In[15]:

def process_tweet(tweet):
    if "text" in tweet:
        try:
            tweet_text = tweet["text"]
            
            if tweet_text.startswith("RT"):
                tweet_text = tweet["retweeted_status"]["extended_tweet"]["full_text"]
                
            if tweet_text not in tweets_set:
                tweets_set.add(tweet_text)
                
                #Detect language if its Malayalam
                lang_detected = translator.detect(tweet_text).lang;
                
                #Translate the text in Malayalam to English
                translated_text = translator.translate(tweet_text, "en").text
                
                if "ml" == lang_detected:
                    print("Original tweet:", tweet_text)
                    print("Translated tweet:", translated_text)
                    
                tweet_text = translated_text
                        
                id_str = tweet["id_str"]
                screen_name = tweet["user"]["screen_name"]
                created_at = tweet["created_at"]
                
                with open('place_tweets.csv', 'a', encoding="utf8") as pf, open('no_place_tweets.csv', 'a', encoding="utf8") as npf:
                    place_writer = csv.writer(pf)
                    no_place_writer = csv.writer(npf)
                    
                    if any(place in tweet_text.lower() for place in kerala_places):
                        row = [id_str, created_at, screen_name, tweet_text, "Twitter"]
                        place_writer.writerow(row) 
                        gSheetsUpdator.insertRow(row)
                    else:
                        no_place_writer.writerow([id_str, created_at, screen_name, tweet_text]) 
        except:
            print("Error while processing tweet:", tweet_text)

    return


# In[16]:

def tweet_consumer():
    while True:
        #print("Inside tweet_consumer...")
        item = tweet_queue.get()
        print("Getting tweet:", item["text"])
        process_tweet(item)
        tweet_queue.task_done()


# In[17]:

def tweet_producer(target_list, twarc):
    if len(target_list) > 0:
        query = ",".join(target_list)
        #print("Processing query:", query)
        
        for tweet in twarc.filter(track = query):
            #print("putting tweet:", tweet["text"])
            tweet_queue.put(tweet)
    return


# In[18]:

if __name__ == '__main__':
    twarc = Twarc(consumer_key, consumer_secret, access_token, access_token_secret)

    #Creating queue and start our consumer thread
    tweet_queue = queue.Queue(1)
    
    consumer_thread = threading.Thread(target=tweet_consumer)
    consumer_thread.daemon=True
    consumer_thread.start()
    
    while True:
        try:
            tweet_producer(target_list, twarc)
        except KeyboardInterrupt:
            print("Keyboard interrupt")
            sys.exit(0)
        except:
            print("Error. Restarting..")
            time.sleep(5)
            pass


# In[ ]:



