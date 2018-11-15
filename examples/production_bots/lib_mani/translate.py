from translate import Translator
from babel import Locale

text="a"

#def translate_to(text,lang):
  #  translator= Translator(to_lang=lang)
   # translation = translator.translate(text)    
   # return translation

def get_lang_disp_name(lang):
    locale = Locale(lang, '')
    return (locale.display_name)

def set_text(text_to_translate):
    global text
    text=text_to_translate

def translate_to(lang):
    translator= Translator(to_lang=lang)
    translation = translator.translate(text)    
    return translation
