# Chapter 4

# Comma code

def commaCode(array):
    num = len(array)
    sentence = '' 
    for i in range(num):
        if i == num-1:
            sentence += 'and ' + array[i]
        else:
            sentence+= array[i] + ' , '
    return sentence

spam = ["apples", "bananas", "tofu", "cats", "mats", "ways"]
commaCode(spam)
print(commaCode(spam))




#I Thought i should inculde my process as i grow to learn form my mistakes
#I need to simplify  
##for i in range(no):
##    if spam[i] != spam[no - 2]:
##       sentence = sentence + spam[i] + " , "
##       print(sentence)
##       print(i) 
##    else:
##        sentence = sentence + " and " + spam[i]
##        print(sentence)
