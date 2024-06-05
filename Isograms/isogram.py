


def is_isogram(string):
    #your code here

    #make the code ignore case and keep track of characteres
    string = string.lower()
    seen =  set()
    #make a for loop for if the character is seen in the set it will return false
    for char in string:
        if char in seen:
            return False
        seen.add(char)
#vomit
    return True






