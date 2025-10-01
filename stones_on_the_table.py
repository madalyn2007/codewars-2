#Stones On The Table

#https://www.codewars.com/kata/5f70e4cce10f9e0001c8995a/train/python

#My function first turns the variable 'stones' into a list, to make it easier to code with.
#Then, it sets the count of the stones to 0
#My function then loops through the list, checking for duplicate stones, starting at 0.
#If the stones next to one another are the same, it adds one to the count.




def solution(stones):
    stoneList = list(stones)
    
    count = 0
    
    for i in range(len(stoneList) - 1):
        if stoneList[i] == stoneList[i+1]:
            count += 1
    return count