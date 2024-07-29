#Words with a_e in them (where the underscore represents any letters) are pronounced like ay_. Given a sentence, create a function which replaces all instances of a_e with a ay_.
#pronounce_the_a_e("i want to bake a cake") ➞ "i want to bayk a cayk"
#pronounce_the_a_e("cinnamon flakes") ➞ "cinnamon flayks"

def pronouncing(word):

    split_word = word.split(" ")
    new = []
    for word in range(len(split_word)):
        if 'a' in split_word[word] and 'e' in split_word[word]:
            for val in range(len(split_word[word])):
                if split_word[word][val] == 'a':
                    if 'e' in split_word[word][val:]:
                        new.append(split_word[word][:val] + 'ay' + split_word[word][val+1:-1])
        else:
            new.append(split_word[word])
    return " ".join(new).strip()
print(pronouncing("bravely escape and inflate"))