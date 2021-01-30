pip install translate

from translate import Translator
translator= Translator(to_lang="Hindi")
translation = translator.translate("you")
print(translation)

from translate import Translator
translator= Translator(from_lang="english",to_lang="Hindi")
input1 = input("enter text>>")
translation = translator.translate(input1)
print(translation)
