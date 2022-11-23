import re
import nltk

class Cleaner:
    def delete_repeated_characters(input_text:str) -> str:
        '''
            input_text : your text
                input : 'ههههههههههههه'
                output: 'هه'
        '''
        pattern  = r'(.)\1{2,}'
        out_text = re.sub(pattern, r"\1\1", input_text)
        return out_text

    def replace_letters(input_text:str) -> str:
        '''
        input_text : your text
            input: 'أهلا وسهلا أجمعين'
            output: 'اهلا وسهلا اجمعين'
        '''
        replace = {"أ": "ا","ة": "ه","إ": "ا","آ": "ا","": ""}
        replace = dict((re.escape(k), v) for k, v in replace.items()) 
        pattern = re.compile("|".join(replace.keys()))
        out_text = pattern.sub(lambda m: replace[re.escape(m.group(0))], input_text)
        return out_text

    def clean_text(input_text:str) -> str:
        replace = r'[/(){}\[\]|@âÂ,;\?\'\"\*…؟–’،!&\+-:؛-]'
        out_text = re.sub(replace, " ", input_text)
        words = nltk.word_tokenize(out_text)
        words = [word for word in words if word.isalpha()]
        out_text = ' '.join(words)
        return out_text

    def remove_vowelization(input_text:str) -> str:
        vowelization = re.compile(""" ّ|َ|ً|ُ|ٌ|ِ|ٍ|ْ|ـ""", re.VERBOSE)
        out_text = re.sub(vowelization, '', input_text)
        return out_text

    def remove_stopword(input_text:str, lang:str= "All") -> str:
        '''
            input_text : your text
            lang : [All:deafult, 'ar', 'en']
        '''
        if lang == "All":
            stop_words = set(nltk.corpus.stopwords.words("arabic") + nltk.corpus.stopwords.words("english"))
            tokenizer = nltk.tokenize.WhitespaceTokenizer()
            tokens = tokenizer.tokenize(input_text)
            wnl = nltk.WordNetLemmatizer()
            lemmatizedTokens =[wnl.lemmatize(t) for t in tokens]
            out_text = [w for w in lemmatizedTokens if not w in stop_words]
            out_text = ' '.join(out_text)
        
        if lang == "ar":
            stop_words = set(nltk.corpus.stopwords.words("arabic"))
            tokenizer = nltk.tokenize.WhitespaceTokenizer()
            tokens = tokenizer.tokenize(input_text)
            wnl = nltk.WordNetLemmatizer()
            lemmatizedTokens =[wnl.lemmatize(t) for t in tokens]
            out_text = [w for w in lemmatizedTokens if not w in stop_words]
            out_text = ' '.join(out_text)
        
        if lang == "en":
            stop_words = set(nltk.corpus.stopwords.words("english"))
            tokenizer = nltk.tokenize.WhitespaceTokenizer()
            tokens = tokenizer.tokenize(input_text)
            wnl = nltk.WordNetLemmatizer()
            lemmatizedTokens =[wnl.lemmatize(t) for t in tokens]
            out_text = [w for w in lemmatizedTokens if not w in stop_words]
            out_text = ' '.join(out_text)
        
        return out_text

    def stem_text(input_text:str) -> str:
        st = nltk.ISRIStemmer()
        tokenizer = nltk.tokenize.WhitespaceTokenizer()
        tokens = tokenizer.tokenize(input_text)
        out_text = [st.stem(w) for w in tokens]
        out_text = ' '.join(out_text)
        return out_text

    def text_prepare(input_text, ar_text:str, lang='All') -> str:
        out_text = Cleaner.delete_links(input_text)
        out_text = Cleaner.delete_repeated_characters(out_text)
        out_text = Cleaner.clean_text(out_text)
        out_text = Cleaner.remove_stopwords(out_text)
        if ar_text:
            out_text = Cleaner.replace_letters(out_text)
            out_text = Cleaner.remove_vowelization(out_text)
            out_text = Cleaner.stem_text(out_text)
        else:
            out_text = out_text.lower()
        return out_text
