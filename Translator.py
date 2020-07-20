# Translate a text file to Japanese from English

from translate import Translator
translator = Translator(to_lang='ja')

try:
    with open('Translate_Me.txt', mode='r') as my_file:
        my_translation = my_file.read()
        translation = translator.translate(my_translation)
        print(translation)  # このページを英語から日本語に翻訳してください。
        with open('./Translated.txt', mode='w', encoding='utf-8') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print('Check your file path silly!')
