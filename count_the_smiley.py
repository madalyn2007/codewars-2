#Count The Smiley Faces!

#https://www.codewars.com/kata/583203e6eb35d7980400002a/train/python

#In my function, I first called 'count' and set it equal to zero.
#Then, I called a loop function to loop through the different faces in the array.
#If the length of the smiley is two characters, then the function checks if the smiley has valid eyes (; or:) and a valid mouth (D or ) ). If so, it adds 1 to the count.
#If the length of the smiley is three characters, then the function checks if the smiley has valid eyes (; or:), a valid nose (~ or -), and a valid mouth (D or ) ). If so, it adds 1 to the count, as well.
#Then, the function returns the count.




def count_smileys(arr):
    count = 0
    
    for face in arr:
        if len(face) == 2:
            if face[0] in ";:" and face[1] in ")D":
                count += 1
        elif len(face) == 3:
            if face[0] in ";:" and face[1] in "~-" and face[2] in ")D":
                count += 1
                
    return count
                    
    pass 