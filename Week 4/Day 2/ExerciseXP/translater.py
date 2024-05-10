from translate import Translator

translator = Translator(from_lang="french", to_lang="english")

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

dict = {}

for el in french_words:
    dict[translator.translate(el)] = el

print(dict)
