def fact(no):
    if no==0 or no==1:
        return 1
    else:
        return (no*fact(no-1))


def num_digit(no):
    sum_digit = 0
    while(no>0):
        digit = no % 10
        sum_digit = sum_digit + fact(digit)
        no = int(no / 10)
    return sum_digit
ans_list = []
num_list = [145,375,0,100,2]
for i in num_list:
    if(i != 0):
        if(i == num_digit(i)):
            ans_list.append(i)
print(ans_list)



'''

def funnn(s):
    for i in range(len(s)-1):
        t = s[i]
        s[i] = s[i+1]
        s[i+1] = t
    return s[:-1]

'''

'''
def fun(str1):
    cout = 1
    str2 = ""
    for i in range(len(str1)-1):
        if(str1[i]==str1[i+1]):
            cout+=1
        else:
            str2 = str2 + str(cout) +str1[i]
            cout=1
    str2 = str2 + str(cout) +str1[i]
    return str2


str3 = input("Enter String ")
str3 = fun(str3)
print(str3)
'''
