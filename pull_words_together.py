#Pull Your Words Together, Man!

#https://www.codewars.com/kata/59ad7d2e07157af687000070/train/python

#First, my function converts the input 'words' to a list, to make it easier to work with.
#Then, it accesses the first word in the new list, uppercasing the first letter and conjoining the rest of the sentence to it.
#The return statement joins the items in the list together, adding a space between words, and then adds a period to the end of the sentence

def sentencify(words):
    wordsList = list(words)
    
    wordsList[0] = words[0][0].upper() + words[0][1:]
    
       
    return " ".join(wordsList) + str(".")

    pass