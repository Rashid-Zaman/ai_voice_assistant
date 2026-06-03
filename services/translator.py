from deep_translator import GoogleTranslator
def translate(transcribed_text,detected_lang):
    
    if detected_lang in ['hi','ur']:
        prompt = GoogleTranslator(
        source="auto",
        target="en"
    ).translate(transcribed_text)
    else:
        prompt=transcribed_text
        
    return prompt

    