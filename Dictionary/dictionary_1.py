import json
#python library for "Text Processing Services"
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

#loading the json data as python dictionary
data = json.load(open("data.json"))

#function for retriving definition
def retirve_definition(word):
    word = word.lower()

    #1st elif: to make sure the program returns definition of words with Capital first letters (Ex: Hello, Rain)
    #2nd elif: to make sure the program returns definition of acronymns (Ex: USA, NFL)
    #str.title(): returns a string which has first letter in each word is uppercase and all remaining letters are lowercase
    #check for non-existing words
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        action = raw_input("Did you mean %s instead? [y or n]: " % get_close_matches(word, data.keys())[0])
        if(action == "y"):
            return data[get_close_matches(word, data.keys())[0]]
        elif(action == "n"):
            return ("The word does not exist yet.")
    else:
        return ("Sorry, the word doesn't exist in this dictionary.")

#input from user
word_user = raw_input("Enter a word: ")

#print(my_function(word_user))

#retrive the definition 
print(retirve_definition(word_user))
