alien_dictionary = {"we": "vorag", "come": "thang", "in": "zon",
"peace": "argh", "hello": "kodar", "can": "znak", "i": "az", "borrow": "liftit",
"some": "zum", "rocket": "upgoman", "fuel": "kakboom", "please": "seplin",}

english_phrase = input("please enter an english word or phrase to translate: ")
english_words = english_phrase.lower().split()

alien_words = []
for word in english_words:
    if word in alien_dictionary:
        alien_words.append(alien_dictionary[word])
    else:
        alien_words.append(word)
print("in alien, say: ", " ".join(alien_words))