import json

#loading the json data as python dictionary
data = json.load(open("data.json"))

#function for retriving definition
def retirve_definition(word):
    #check for non-existing words
    if word in data:
        return data[word]
    else:
        return ("Sorry, the word doesn't exist in this dictionary.")

#input from user
word_user = raw_input("Enter a word: ")

#print(my_function(word_user))

#retrive the definition 
print(retirve_definition(word_user))
