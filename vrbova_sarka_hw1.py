import json

with open("alice.txt", encoding="utf-8") as homework_file:
    text = homework_file.read().lower()
    
number_of_characters = {}
for character in text:
    if character != " " and character != "\n":
        if character not in number_of_characters:
            number_of_characters[character] = 1
        else:
            number_of_characters[character] += 1
sorted_dictionary = dict(sorted(number_of_characters.items()))

with open("hw_output.json", mode = "w", encoding="utf-8") as file_json:
    json.dump(sorted_dictionary, file_json)