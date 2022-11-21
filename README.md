# PyShbak
 ![image](https://github.com/AbdelrahmanShahrour/PyShbak/blob/main/logo/SHAWPACK-LOGO.png?raw=true) 

###  Now with PyShbak, dealing with Arabic texts has become easy, and in the future it will become easier with PyShbak 

## Installation

```python
pip3 install PyShbak
```
---
## Structure 

|> PyShbak

| ------> | `Normalization`

|---------| ------> | `Normalization_ar`

|---------|---------| ------> | alef

|---------|---------| ------> | lamalef

|---------|---------| ------> | hamza

|---------|---------| ------> | tah

|---------|---------| ------> | madah

|---------|---------| ------> | normalization_all

| ------> `Processor`

|---------| ------> | `Arabic_Processor`

|---------|---------| ------> | remove_stopword

|---------|---------| ------> | remove_other_lang

|---------|---------| ------> | remove_diacritics

|---------|---------| ------> | remove_arabic_punctuations

|---------|---------| ------> | arabic_only

|---------|---------| ------> | with_out_num

|---------| ------> | `English_Processor`

|---------|---------| ------> | remove_stopword

|---------|---------| ------> | english_only

|---------|---------| ------> | remove_english_punctuations

|---------|---------| ------> | with_out_num

|---------| ------> | `General_Processor`

|---------|---------| ------> | remove_mentions

|---------|---------| ------> | remove_hasgtag

|---------|---------| ------> | remove_links

|---------|---------| ------> | remove_punctation

|---------|---------| ------> | keep_text

|---------|---------| ------> | remove_emojis

|---------|---------| ------> | remove_whitespace

---

## Example:

```python
pip3 install PyShbak
```

```python
from PyShbak.TweetsCleaner import Clean_tweet
```



```python
text = 'akhhh !تَوقَعْت إذا جات داريا بشوفهم كاملين بس لي للحين احس فيه احد ناقْصهم 💔 #Avlu https://www.messenger.com/ @PyShbak '

Clean_tweet.ar(text)
```

output:
`' توقعت اذا جات داريا بشوفهم كاملين بس لي للحين احس فيه احد ناقصهم '
`