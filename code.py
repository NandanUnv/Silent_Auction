
import os
print('------------------')
print("welcome to auction")
print('------------------')

dic = {}
while True:
    a = input("What is your name?:")
    b = int(input("What is you bid no:"))
    dic[a]=b
    c = input("Is there any other bider?(Y/N):")

    if c =='y' or c =='Y':
        os.system('cls')
    else:
        break

max = 0
l = list(dic.keys())
k = list(dic.values())
for i in range(len(k)):
    if max<k[i]:
        max=k[i]

print('list of all persons along their bid:\n',dic)
print(f"The auction is won by {l[k.index(max)]} with bid of {max}")
print('---------')
print('Thank You')
print('---------')
