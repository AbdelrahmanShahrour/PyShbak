import re

from PyShbak.ar import *
from PyShbak.en import *
from PyShbak.general import *

class Normalization_ar:
    def alef(text:str) -> str:
        for tam in ALEF_CHARS:
            text = text.replace(tam, NORMAL_ALEF)
        return text

    def lamalef(text:str) -> str:
        for tam in LAM_ALEF_COMBINED:
            text = text.replace(tam, LAM_ALEF_NORMAL)
        return text

    def hamza(text:str) -> str:
        for tam in HAMZA_CHARS:
            print(tam)
            text = text.replace(tam, NORMAL_HAMZA)
            print(text)
        return text

    
    def tah(text:str) -> str:
        text = text.replace(TAH_MARBOTA, HA)
        return text


    def madah(text:str) -> str:
        text = text.replace(TATWEEL, "")
        return text
    
    def normalization_all(text:str) -> str:
        text = Normalization_ar.alef(text)
        text = Normalization_ar.lamalef(text)
        text = Normalization_ar.hamza(text)
        text = Normalization_ar.tah(text)
        return text
