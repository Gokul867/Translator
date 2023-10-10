
from translate import Translator

translator = Translator(to_lang="pt")
try:
    with open(".\english.txt", mode='r') as myfile:
        text = myfile.read()
        print(text)

except FileNotFoundError as e:
    print("OOPS File NOT FOUND")

print(text)
translation = translator.translate(text)
print(translation)
