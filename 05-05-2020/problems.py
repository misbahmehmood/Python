'''def one(input1, input2):
    if len(input1)==len(input2):
        full= input1 + " " + input2
        return full
    elif len(input1)>len(input2):
    	return input1
    elif len(input2)> len(input1):
        return input2
    return one
firstinput= input('enter first string: ')
second= input('enter second string: ')
print(one(firstinput, second))'''
    


'''def three(arg1):
    if arg1 % 3 ==0:
        return 'fizz'
    if arg1 % 5 ==0:
        return 'buzz'
    if (arg1 % 3==0) and (arg1 % 5==0):
        return 'fizzbuzz'
    return 'null'''

'''def six(input):
    for i in range(len(input)):
        if input[i]=='i':
            return input[i+1]=='e'
        return False
    
print(six('cieling'))'''


    
    	

'''def eight(facto):
    number = 1
    for i in range(1,facto+1):
        number*=i
    return number
input = int(input("enter number between 1 and 10: "))
    if input >10 or input <1:
        return 0
print(eight(input))'''


'''def nine(inputstring, char):
    if char in inputstring:
        return inputstring.find(char)
   
print(nine("This is a Sentence"))'''


def seven(case):
    count= 0
    vowel='aeiou'
    vowel1=vowel.lower()
    for i in case:
            if vowel in case:
                count+=1

    return count
print(seven('goodbye'))