inputString = sorted(input())
lowerCase = ''
upperCase = ''
oddInt = ''
evenInt = ''

for i in inputString:
    
    if i.isupper():
        upperCase = upperCase + i
        
    if i.islower():
        lowerCase = lowerCase + i
        
    if i.isnumeric():
        if int(i)%2 == 0:
            evenInt = evenInt + i
            
        if int(i)%2 != 0:
            oddInt = oddInt + i
            
print(lowerCase+upperCase+oddInt+evenInt)

