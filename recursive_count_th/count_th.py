'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# My notes start here: 

# Add count into the parameter and set it to equal to 0.
def count_th(word, count = 0):
    
    # TBC
    
    # Make an if statement of if the length of word is less than 2, then return the count.
    if len(word) < 2:
        return count
    
    # if the beginning of the word contains 'th', then add to the count and then repeat the recursion.
    if word[0:2] == 'th':
        count = count + 1
       
    # Return the count_th with word[1:] and Move up one letter and check if new [0:2] are 'th'. 
    return count_th(word[1:], count)
    
