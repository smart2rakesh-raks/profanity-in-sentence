import re

slurs_word =["bad","shit"]
tweet =[]
with open("E:/assigment/91social/file.txt", 'r') as file:
    for i in file:
        tweet.append(i)
    for j in tweet:
        words = re.split(' |\n', j)
        degree = 0
        for k in words:
            if k in slurs_word:
                degree += 1
        if degree is not None:
            print('Degree of profanity sentence '+str(degree))



