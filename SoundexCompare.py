'''
Created on 18-Aug-2018

Util class related to Soundex
@author: sethu
'''

from fuzzy import Soundex

class SoundexUtil():
    soundex = Soundex(4)
    
    def matches(self, str1, str2):
        
        str1_soundex = SoundexUtil.soundex(str1)
        str2_soundex = SoundexUtil.soundex(str2)
        
        return str1_soundex == str2_soundex
    
    def getSoundexMatch(self, input_str, target_list):
        for word in input_str.split():
            for target_word in target_list:
                print("word:", word)
                print("target_word:", target_word)
                if self.matches(word, target_word):
                    return word
        return None
    
if __name__ == '__main__':
    kerala_places=["alappuzha","ambalapuzha","chengannur","cherthala","karthikappally","kuttanad","mavelikkara","kakkanad","aluva","kanayannur","kochi","kothamangalam","kunnathunad","muvattupuzha","paravur","idukki","painavu","devikulam","peerumade","thodupuzha","udumbanchola","kannur","thalassery","thalipparamba","kasaragod","hosdurg","kollam","karunagappally","kottarakkara","kunnathur","pathanapuram","kottayam","changanasserry","kanjirappally","meenachil","vaikom","kozhikode","koyilandy","vadakara","malappuram","eranad","nilambur","perinthalmanna","ponnani","tirur","tirurangadi","palakkad","alathur","chittur","mannarkkad","ottappalam","pathanamthitta","adoor","kozhencherry","mallappally","ranni","thiruvalla","thiruvananthapuram","chirayinkeezhu","nedumangad","neyyattinkara","thrissur","chavakkad","kodungallur","mukundapuram","thalapilly","wayanad","kalpetta","mananthavady","sultanbattery","vythiri","haripad","mankombu","ernakulam","perumbavoor","northparavur","painavu    ","peermade","nedumkandam","iritty","payyanur","manjeshwaram","uppala","vellarikundu","chathannoor","sasthamkotta","punalur","palai","thamarassery","vatakara","7taluks[22]","manjeri(eranad)","kondotty","pattambi","konni","hiruvananthapuram","kattakada","attingal","varkala","irinjalakuda","chalakudy","wadakkancheri","kunnamkulam","taliparamba","udma","vallachira","varam","nenmenikkara","paduvilayi","palissery","panniyannur","panoor","pappinisseri","paravoor","pathiriyad","pattiom","payyannur","peralasseri","peringathur","pinarayi","pottore","puranattukara","puthukkad","quilandy","shoranur","narath","kannapuram","kayamkulam","kolazhy","koothuparamba","koratty","kottayam-malabar","manjeshwar","marathakkara","mattannur","mavilayi","mavoor","munderi","kanhangad","kanhirode","kanjikkuzhi","kannadiparamba","bangramanjeshwar","chala","changanassery","chelora","chendamangalam","cheruthazham","chevvoor","chittur","thathamangalam","chockli","erattupetta","guruvayoor","hosabettu","idukkitownship","iriveri","kadirur","kalliasseri","akathiyoor","ancharakandy","arookutty","aroor","avinissery"]
    str1 = "the is no water in kottayam"
    soundexUtil = SoundexUtil()
    print(soundexUtil.getSoundexMatch(str1, kerala_places))