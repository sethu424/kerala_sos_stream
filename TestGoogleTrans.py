'''
Created on 18-Aug-2018

@author: sethu
'''

from googletrans import Translator

if __name__ == '__main__':
    translator = Translator()
    translations = translator.translate("ഒരു നാട് മുഴുവൻ ഇവിടെ ഒറ്റക്കെട്ടായി പ്രെളയത്തെ നേരിടുമ്പോളും പശുവിനു പന്നിയിൽ ഉണ്ടായ ഇവനെ പോലുള്ളവന്മാർക്ക് വിധ്വെഷം വിളമ്പാനെ അറിയൂ.. ആലുവ റിലൈൻസ് ഫ്രഷ് ദുരിതാശ്വാസ വിതരണത്തെ ആളുകളുടെ കയ്യേറ്റമാക്കി... https://twitter.com/nach1keta/status/1030712526743515136?s=21 …", "en")
    print(translations.text)
    #print(translator.detect("ഒരു നാട് മുഴുവൻ ").lang)