#Credit Card Mask

#https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python

#First, my funtion asks if the length of the string is less than 4. If so, it just returns the original string, as there is no need to censor anything.
#If the strinf is longer, it takes the length of the string, subtracts four from it, keeping the last 4 digits visible, and then multiplies the string by '#' to tag out whats left
#Then, it slices starting at the 4th to last character to the end of the string, preserving the original last 4 digits 

def maskify(cc):
    if len(cc)  <= 4:
        return cc
    else:
        taggedText = "#" * (len(cc) - 4)
        lastDigit = cc[-4:]
        return taggedText + lastDigit

    pass