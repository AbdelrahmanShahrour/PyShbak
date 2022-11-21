from PyShbak.Processor import *
from PyShbak.Normalization import *

class Clean_tweet:
    def ar(tweet:str, Normalize_all:str='No') -> str:
        '''
        tweet is your text.
        Normalize_all : 'No' or 'Yes'
        '''
        tweet = General_Processor.remove_hasgtag(tweet)
        tweet = General_Processor.remove_links(tweet)
        tweet = General_Processor.remove_mentions(tweet)
        tweet = General_Processor.remove_whitespace(tweet)
        tweet = Arabic_Processor.remove_arabic_punctuations(tweet)
        tweet = Arabic_Processor.remove_diacritics(tweet)
        tweet = Arabic_Processor.remove_other_lang(tweet)
        if Normalize_all == "Yes":
            tweet = Normalization_ar.normalization_all(tweet)
        tweet = General_Processor.remove_emojis(tweet)
        return tweet
    
    def en(tweet:str) -> str:
        tweet = General_Processor.remove_hasgtag(tweet)
        tweet = General_Processor.remove_links(tweet)
        tweet = General_Processor.remove_mentions(tweet)
        tweet = General_Processor.remove_whitespace(tweet)
        tweet = English_Processor.remove_english_punctuations(tweet)
        tweet = English_Processor.english_only(tweet)
        tweet = General_Processor.remove_emojis(tweet)
        return tweet
