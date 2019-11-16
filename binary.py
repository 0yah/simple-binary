import math



def binary(num):
    bits =[]
    result=int(math.log2(num))
    #print("{} {} \n".format(num,result))
    bits.append(result)

    while result != 0:
        num=num-(2**result)
        if num == 0:
            break
        result=int(math.log2(num))
        #print("{} {} \n".format(num,result))
        bits.append(result)

    return bits



def print_binary(user_num):
    bits=binary(user_num)
    answer =0
    for bit in bits:
        answer = answer + (10**bit)
    print(answer)

user_num=input("Enter the number you want to change to binary\n")
user_num= int(user_num)
print_binary(user_num)

#ascii  65 - 90 capital case

upper=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower =[]
for up in upper:
    #changes the list with capital characters to lower characters
    lower.append(up.lower())

index=0
my_ascii = {}
for i in range(65,91):# 65- 91 ASCII lower case
    #associates each decimal number with its upper case ascii equivalent
    my_ascii[upper[index]] = i
    index += 1 

index=0
for p in range(97,123):# 97- 122 ASCII lower case  
    #associates each decimal number with its lower case ascii equivalent
    my_ascii[lower[index]] = p
    index += 1 

#print(my_ascii)

input_strings = input("Enter the string you want to change to binary\n")

#loop through each character in the entered string
for bn in input_strings:
    #print(my_ascii[bn])

    #change each character to binary and display it
    ascii_bin=my_ascii[bn]
    print_binary(ascii_bin)