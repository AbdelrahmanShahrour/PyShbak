import re

from nltk import word_tokenize

from PyShbak.ar import *
from PyShbak.en import *
from PyShbak.general import *


class Arabic_Processor:
    def remove_stopword(text:str) -> str:
        '''
        text: your data.
        remove this words
        stop_word_ar = ['إذ', 'إذا', 'إذما', 'إذن', 'أف', 'أقل', 'أكثر', 'ألا', 'إلا', 'التي', 'الذي',
         'الذين', 'اللاتي', 'اللائي', 'اللتان', 'اللتيا', 'اللتين', 'اللذان', 'اللذين', 'اللواتي',
         'إلى', 'إليك', 'إليكم', 'إليكما', 'إليكن', 'أم', 'أما', 'أما', 'إما', 'أن', 'إن', 
        'إنا', 'أنا', 'أنت', 'أنتم', 'أنتما', 'أنتن', 'إنما', 'إنه', 'أنى', 'أنى', 'آه', 'آها', 'أو', 
        'أولاء', 'أولئك', 'أوه', 'آي', 'أي', 'أيها', 'إي', 'أين', 'أين', 'أينما', 
        'إيه', 'بخ', 'بس', 'بعد', 'بعض', 'بك', 'بكم', 'بكم', 'بكما', 'بكن', 'بل', 'بلى',
         'بما', 'بماذا', 'بمن', 'بنا', 'به', 'بها', 'بهم', 'بهما', 'بهن', 'بي', 
        'بين', 'بيد', 'تلك', 'تلكم', 'تلكما', 'ته', 'تي', 'تين', 'تينك', 'ثم', 'ثمة', 
        'حاشا', 'حبذا', 'حتى', 'حيث', 'حيثما', 'حين', 'خلا', 'دون', 'ذا', 'ذات', 'ذاك', 'ذان',
         'ذانك', 'ذلك', 'ذلكم', 'ذلكما', 'ذلكن', 'ذه', 'ذو', 'ذوا', 'ذواتا', 'ذواتي', 'ذي', 'ذين',
         'ذينك', 'ريث', 'سوف', 'سوى', 'شتان', 'عدا', 'عسى', 'عل', 'على', 'عليك', 'عليه', 'عما',
         'عن', 'عند', 'غير', 'فإذا', 'فإن', 'فلا', 'فمن', 'في', 'فيم', 'فيما', 'فيه', 'فيها',
         'قد', 'كأن', 'كأنما', 'كأي', 'كأين', 'كذا', 'كذلك', 'كل', 'كلا', 'كلاهما', 'كلتا',
         'كلما', 'كليكما', 'كليهما', 'كم', 'كم', 'كما', 'كي', 'كيت', 'كيف', 'كيفما', 'لا', 'لاسيما',
         'لدى', 'لست', 'لستم', 'لستما', 'لستن', 'لسن', 'لسنا', 'لعل', 'لك', 'لكم', 'لكما',
        'لكن', 'لكنما', 'لكي', 'لكيلا', 'لم', 'لما', 'لن', 'لنا', 'له', 'لها', 'لهم', 
        'لهما', 'لهن', 'لو', 'لولا', 'لوما', 'لي', 'لئن', 'ليت', 'ليس', 'ليسا', 'ليست', 
        'ليستا', 'ليسوا', 'ما', 'ماذا', 'متى', 'مذ', 'مع', 'مما', 'ممن', 'من', 'منه', 'منها',
         'منذ', 'مه', 'مهما', 'نحن', 'نحو', 'نعم', 'ها', 'هاتان', 'هاته', 'هاتي', 'هاتين', 
        'هاك', 'هاهنا', 'هذا', 'هذان', 'هذه', 'هذي', 'هذين', 'هكذا', 'هل', 'هلا', 'هم', 'هما', 'هن',
         'هنا', 'هناك', 'هنالك', 'هو', 'هؤلاء', 'هي', 'هيا', 
        'هيت', 'هيهات', 'والذي', 'والذين', 'وإذ', 'وإذا', 'وإن', 'ولا',
         'ولكن', 'ولو', 'وما', 'ومن', 'وهو', 'يا', 'أبٌ', 'أخٌ', 'حمٌ', 'فو', 'أنتِ', 'يناير',
         'فبراير', 'مارس', 'أبريل', 'مايو', 'يونيو', 'يوليو', 'أغسطس', 'سبتمبر', 'أكتوبر',
         'نوفمبر', 'ديسمبر', 'جانفي', 'فيفري', 'مارس', 'أفريل', 'ماي', 'جوان', 'جويلية', 
        'أوت', 'كانون', 'شباط', 'آذار', 'نيسان', 'أيار', 'حزيران', 'تموز', 'آب', 
        'أيلول', 'تشرين', 'دولار', 'دينار', 'ريال', 'درهم', 'ليرة', 'جنيه', 'قرش', 'مليم', 
        'فلس', 'هللة', 'سنتيم', 'يورو', 'ين', 'يوان', 'شيكل', 'واحد', 'اثنان', 'ثلاثة', 
        'أربعة', 'خمسة', 'ستة', 'سبعة', 'ثمانية', 'تسعة', 'عشرة', 'أحد', 'اثنا', 'اثني', 'إحدى', 
        'ثلاث', 'أربع', 'خمس', 'ست', 'سبع', 'ثماني', 'تسع', 'عشر', 'ثمان', 'سبت', 'أحد',
         'اثنين', 'ثلاثاء', 'أربعاء', 'خميس', 'جمعة', 'أول', 'ثان', 'ثاني', 'ثالث', 
        'رابع', 'خامس', 'سادس', 'سابع', 'ثامن', 'تاسع', 'عاشر', 
        'حادي', 'أ', 'ب', 'ت', 
        'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 
        'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف',
         'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي', 'ء', 'ى', 'آ', 'ؤ', 'ئ', 'أ', 'ة', 'ألف', 
        'باء', 'تاء', 'ثاء', 'جيم', 'حاء', 'خاء', 'دال', 'ذال', 
        'راء', 'زاي', 'سين', 'شين', 'صاد', 'ضاد', 'طاء', 'ظاء',
         'عين', 'غين', 'فاء', 'قاف', 'كاف', 'لام', 'ميم', 'نون',
         'هاء', 'واو', 'ياء', 'همزة', 'ي', 'نا', 'ك', 'كن', 'ه',
         'إياه', 'إياها', 'إياهما', 'إياهم', 'إياهن', 'إياك', 'إياكما', 'إياكم',
         'إياك', 'إياكن', 'إياي', 'إيانا', 'أولالك', 'تانِ', 'تانِك', 'تِه', 'تِي', 'تَيْنِ',
         'ثمّ', 'ثمّة', 'ذانِ', 'ذِه', 'ذِي', 'ذَيْنِ', 'هَؤلاء', 
        'هَاتانِ', 'هَاتِه', 'هَاتِي', 'هَاتَيْنِ', 'هَذا', 'هَذانِ', 'هَذِه', 
        'هَذِي', 'هَذَيْنِ', 'الألى', 'الألاء', 'أل', 'أنّى', 'أيّ', 'ّأيّان', 'أنّى', 'أيّ',
         'ّأيّان', 'ذيت', 'كأيّ', 'كأيّن', 'بضع', 'فلان', 'وا', 'آمينَ',
         'آهِ', 'آهٍ', 'آهاً', 'أُفٍّ', 'أُفٍّ', 'أفٍّ', 'أمامك', 'أمامكَ', 'أوّهْ', 
        'إلَيْكَ', 'إلَيْكَ', 'إليكَ', 'إليكنّ', 'إيهٍ', 'بخٍ', 'بسّ', 'بَسْ', 'بطآن', 'بَلْهَ', 'حاي',
         'حَذارِ', 'حيَّ', 'حيَّ', 'دونك', 'رويدك', 'سرعان', 'شتانَ', 
        'شَتَّانَ', 'صهْ', 'صهٍ', 'طاق', 'طَق', 'عَدَسْ', 'كِخ', 'مكانَك', 
        'مكانَك', 'مكانَك', 'مكانكم', 'مكانكما', 'مكانكنّ',
         'نَخْ', 'هاكَ', 'هَجْ', 'هلم', 'هيّا', 'هَيْهات', 'وا', 'واهاً', 'وراءَك',
         'وُشْكَانَ', 'وَيْ', 'يفعلان', 'تفعلان', 'يفعلون', 'تفعلون',
         'تفعلين', 'اتخذ', 'ألفى', 'تخذ', 
        'ترك', 'تعلَّم', 'جعل', 'حجا', 'حبيب', 'خال',
         'حسب', 'خال', 'درى', 'رأى', 'زعم', 
        'صبر', 'ظنَّ', 'عدَّ', 'علم', 'غادر', 
        'ذهب', 'وجد', 'ورد', 'وهب', 'أسكن', 'أطعم', 
        'أعطى', 'رزق', 'زود', 'سقى', 'كسا', 'أخبر', 
        'أرى', 'أعلم', 'أنبأ', 'حدَث', 'خبَّر', 'نبَّا',
         'أفعل به', 'ما أفعله', 'بئس', 'ساء', 'طالما',
         'قلما', 'لات', 'لكنَّ', 'ءَ', 'أجل', 
         'إذاً', 'أمّا', 'إمّا', 'إنَّ', 'أنًّ', 'أى', 'إى',
         'أيا', 'ب', 'ثمَّ', 'جلل', 'جير', 'رُبَّ', 'س', 
        'علًّ', 'ف', 'كأنّ', 'كلَّا', 'كى', 'ل', 'لات', 
        'لعلَّ', 'لكنَّ', 'لكنَّ', 'م', 'نَّ', 'هلّا', 'وا', 'أل', 'إلّا', 
        'ت', 'ك', 'لمّا', 'ن', 'ه', 'و', 'ا', 'ي', 
        'تجاه', 'تلقاء', 'جميع', 'حسب', 'سبحان', 'شبه', 'لعمر', 
        'مثل', 'معاذ', 'أبو', 'أخو', 'حمو', 'فو',
         'مئة', 'مئتان', 'ثلاثمئة', 'أربعمئة',
         'خمسمئة', 'ستمئة', 'سبعمئة', 'ثمنمئة', 'تسعمئة',
         'مائة', 'ثلاثمائة', 'أربعمائة', 'خمسمائة', 'ستمائة',
         'سبعمائة', 'ثمانمئة', 'تسعمائة', 'عشرون', 'ثلاثون', 'اربعون', 
        'خمسون', 'ستون', 'سبعون', 'ثمانون', 'تسعون', 'عشرين', 'ثلاثين', 
        'اربعين', 'خمسين', 'ستين', 'سبعين', 
        'ثمانين', 'تسعين', 'بضع', 'نيف', 'أجمع', 
        'جميع', 'عامة', 'عين', 'نفس', 'لا سيما', 
        'أصلا', 'أهلا', 'أيضا', 'بؤسا',
         'بعدا', 'بغتة', 'تعسا', 'حقا', 'حمدا', 
        'خلافا', 'خاصة', 'دواليك', 'سحقا', 'سرا', 'سمعا', 
        'صبرا', 'صدقا', 'صراحة', 'طرا', 'عجبا', 'عيانا', 
        'غالبا', 'فرادى', 'فضلا', 'قاطبة', 'كثيرا', 'لبيك',
         'معاذ', 'أبدا', 'إزاء', 'أصلا', 'الآن', 'أمد', 'أمس', 'آنفا', 
        'آناء', 'أنّى', 'أول', 'أيّان', 'تارة', 'ثمّ', 'ثمّة', 'حقا',  
        'صباح', 'مساء', 'ضحوة', 'عوض', 'غدا', 'غداة', 'قطّ', 'كلّما',
         'لدن', 'لمّا', 'مرّة', 'قبل', 'خلف', 'أمام', 'فوق', 'تحت', 'يمين', 
        'شمال', 'ارتدّ', 'استحال', 'أصبح', 'أضحى', 'آض', 'أمسى',
         'انقلب', 'بات', 'تبدّل', 'تحوّل', 'حار', 'رجع', 'راح', 'صار', 'ظلّ',
         'عاد', 'غدا', 'كان', 'ما انفك', 'ما برح', 'مادام',
        'مازال', 'مافتئ', 'ابتدأ', 'أخذ', 'اخلولق', 'أقبل', 'انبرى', 'أنشأ', 'أوشك', 
        'جعل', 'حرى', 'شرع', 'طفق', 'علق', 'قام', 'كرب', 'كاد', 'هبّ']

        '''
        text = text.split(' ')
        words = [word for word in text if word not in stop_word_ar]
        output = ' '.join(words)
        return output
    
    def remove_other_lang(text : str) -> str:
        '''
            = Keep ARABIC PUNCTUATION
            text : "أَهْلًا وسَهْلًا Hello 212"
            output : 
                ---> "أهلا وسهلا"
        '''
        chars = [char for char in text if ((char in ARABIC_CHARS) or (char in ARABIC_NUM) or (char in ARABIC_PUNCTUATION))]
        output = ''.join(chars)
        return output

    def remove_diacritics(text : str) -> str:
        '''
            text : "أَهْلًا وسَهْلًا Hello 212"
            output : 
                ---> "أهلا وسهلا Hello 212"
        '''
        chars = [char for char in text if (char not in HARAKAT)]
        output = ''.join(chars)
        return output

    def remove_arabic_punctuations(text : str) -> str:
        '''
            text : ", أَهْلًا وسَهْلًا Hello 212"
            output : 
                ---> "  أَهْلًا وسَهْلًا Hello 212"
        '''
        chars = [char for char in text if (char not in ARABIC_PUNCTUATION)]
        output = ''.join(chars)
        return output
    

    def arabic_only(text:str, numbers='No') -> str:
        '''
            text : "أهلا وسهلا 122 hello ٣٤".
            numbers : 
                -> No is a deafult value.
                    output : 
                    --->> "أهلا وسهلا"
                -> Yes : keep arabic lang with arabic num.
                    output : 
                    --->> "أهلا وسهلا ٣٤"
                -> All : keep arabic lang with all num.
                    output : 
                    --->> "أهلا وسهلا 122 ٣٤"
        '''
        if numbers not in ["No", "Yes", "All"]:
            numbers = "No"
        
        if numbers == "No":
            chars = [char for char in text if char in ARABIC_CHARS]
            output = ''.join(chars)
        elif numbers == "Yes":
            chars = [char for char in text if (char in ARABIC_CHARS) or (char in ARABIC_NUM)]
            output = ''.join(chars)
        elif numbers == "All":
            chars = [char for char in text if (char in ARABIC_CHARS) or (char in ARABIC_NUM) or (char in ENGLISH_NUM)]
            output = ''.join(chars)
        return output

    
    def with_out_num(text:str) -> str:
        '''
            text : "أهلا وسهلا 122 hello ٣٤".
                output : 
                --->  "أهلا وسهلا 122 hello ".
        '''
        chars = [char for char in text if (char not in ARABIC_NUM)]
        output = ''.join(chars)
        return output
    


class English_Processor:
    def remove_stopword(text:str) -> str:
        pass

    def english_only(text:str, numbers = "No") -> str:
        '''
            text : "أهلا وسهلا 122 hello ٣٤".
            numbers : 
                -> No is a deafult value.
                    output : 
                    --->> "hello
                -> Yes : keep english lang with english num.
                    output : 
                    --->> "122 hello "
                -> All : keep english lang with all num.
                    output : 
                    --->> "122 hello ٣٤"
        '''
        if numbers not in ["No", "Yes", "All"]:
            numbers = "No"
        
        if numbers == "No":
            chars = [char for char in text if char in ENGLISH_CHARS]
            output = ''.join(chars)
        elif numbers == "Yes":
            chars = [char for char in text if (char in ENGLISH_CHARS) or (char in ENGLISH_NUM)]
            output = ''.join(chars)
        elif numbers == "All":
            chars = [char for char in text if (char in ENGLISH_CHARS) or (char in ARABIC_NUM) or (char in ENGLISH_NUM)]
            output = ''.join(chars)
        return output


    
    def remove_english_punctuations(text:str) -> str:
        '''
            text : "أَهْلًا وسَهْلًا Hello 212 , ?"
            output : 
                ---> "أَهْلًا وسَهْلًا Hello 212"
        '''
        chars = [char for char in text if (char not in ENGLISH_PUNCTUATION)]
        output = ''.join(chars)
        return output

    
    def with_out_num(text:str) -> str:
        '''
            text : "أهلا وسهلا 122 hello ٣٤".
                output : 
                --->  "أهلا وسهلا  hello ٣٤".
        '''

        chars = [char for char in text if (char not in ENGLISH_NUM)]
        output = ''.join(chars)
        return output


class General_Processor:
    def remove_mentions(text: str) -> str:
        '''
            text : 'هدف لا نراه كل يوم . #LEITOT . @oki_q8e شوف ابن اختي شوف 🤗 https://t.co/ZmVMl4sOqA'
                output : 
                ---> 'هدف لا نراه كل يوم . #LEITOT . شوف ابن اختي شوف 🤗 https://t.co/ZmVMl4sOqA'
        
        '''
        output = re.sub(r" @[\w_]+ | @[\w_]+|^@[\w_]+ ", " ", string = text)
        return output
    
    def remove_hasgtag(text:str) -> str:
        '''
            text : 'هدف لا نراه كل يوم . #LEITOT . @oki_q8e شوف ابن اختي شوف 🤗 https://t.co/ZmVMl4sOqA'
                output : 
                ---> 'هدف لا نراه كل يوم . . @oki_q8e شوف ابن اختي شوف 🤗 https://t.co/ZmVMl4sOqA'
        
        '''
        output = re.sub(r"#.*?(?=\s)", "", string=text)
        return output
    
    def remove_links(text: str) -> str:
        '''
            text : 'هدف لا نراه كل يوم . #LEITOT . @oki_q8e شوف ابن اختي شوف 🤗 https://t.co/ZmVMl4sOqA'
                output : 
                ---> 'هدف لا نراه كل يوم . #LEITOT . @oki_q8e شوف ابن اختي شوف 🤗 '
        
        '''
        output = re.sub("http[s]?://\S+|[wW]{3,}[\S/\?=\.&]+", "", string=text)
        return output
    
    def remove_punctation(self, text: str) -> str:
        '''
            text : 'هدف لا نراه كل يوم . #LEITOT . @oki_q8e شوف ابن اختي شوف 🤗 https://t.co/ZmVMl4sOqA'
                output : 
                ---> 'هدف لا نراه كل يوم  LEITOT  okiq8e شوف ابن اختي شوف 🤗 httpstcoZmVMl4sOqA'
        
        '''

        chars = [char for char in text if (char not in PUNCTUATION)]
        output = ''.join(chars)
        return output
    
    def keep_text(self, text:str) -> str:
        '''
            text : 'هدف لا نراه كل يوم . #LEITOT . @oki_q8e شوف ابن اختي شوف 🤗 https://t.co/ZmVMl4sOqA'

                output : 
                ---> 'هدف لا نراه كل يوم  LEITOT  okiq8e شوف ابن اختي شوف httpstcoZmVMl4sOqA'
        
        '''
        chars = [char for char in text if (char in ARABIC_CHARS) or (char in ENGLISH_CHARS)]
        output = ''.join(chars)
        return output
    
    def remove_emojis(text:str) -> str:
        '''
            text : 'هدف لا نراه كل يوم . #LEITOT . @oki_q8e شوف ابن اختي شوف 🤗 https://t.co/ZmVMl4sOqA'

                output : 
                ---> 'هدف لا نراه كل يوم . #LEITOT . @oki_q8e شوف ابن اختي شوف  https://t.co/ZmVMl4sOqA'
        
        '''
        emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
        output = re.sub(emoj, '', text)
        return output

    def remove_whitespace(text: str, keep_spaces=1) -> str:
        '''
            text: "ff       ff  ff"
                output : 
                ---> 'ff ff ff'

        '''
        return re.sub(" +", " " * keep_spaces, "".join(text))

