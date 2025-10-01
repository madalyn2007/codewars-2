#Easy Time Convert

#https://www.codewars.com/kata/5a084a098ba9146690000969/train/python

#My function checks if the variable 'num' is less than zero, and then sets 'num' to 0 if so. 
#It then defines hours and minutes, converting 'num' by dividing it by 60 or by using the modulus operator by the number of minutes.
#Then, the funtion returns the answer as a formatted string. 
#The specifer, '02d' states that the hours/minutes should be padded with a 0, should be 2 digits long, and should be an integer.


def time_convert(num):
    
    if num < 0:
        num = 0
    
    hours = num // 60
    minutes = num % 60
    
    
    return f"{hours:02d}:{minutes:02d}"