import json
#python library for "Text Processing Services"
import difflib
from difflib import SequenceMatcher

#loading the json data as python dictionary
data = json.load(open("data.json"))

#run a Sequence matcher
#first param is junk, includes spaces, blank lines, etc
#second and third param are the words to find similarities in-between
# Ratio is used to find how close those two words are in numerical terms
value = SequenceMatcher(None, "rainn", "rain").ratio()
print(value)

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
    else:
        return ("Sorry, the word doesn't exist in this dictionary.")

#input from user
word_user = raw_input("Enter a word: ")

#print(my_function(word_user))

#retrive the definition 
print(retirve_definition(word_user))
