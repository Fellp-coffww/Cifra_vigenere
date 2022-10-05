import re
from string import ascii_lowercase as lc


frase = str(input("Digite a frase a ser incriptada: "))
key = str(input("Digite sua chave: "))

intlk = 0
result = ""
incript = re.split(r'(.)', frase)
key_idx  = re.split(r'(.)', key)
incript2 = []
key_idx2 = []

for x in incript:
    if x != '' :
        incript2.append(x)

for x in key_idx:
    if x != '' :
        key_idx2.append(x)

newphrase = []
loop = 0
while intlk < len(incript2):
    if loop > len(key_idx2):
        loop = 0
    else:
     num = lc.find(incript2[intlk])
     num2 = lc.find(key_idx2[loop])
     word = (num - num2) % 26
     newphrase.append(lc[word])
     intlk += 1

for x in newphrase:
    result += x

print(result)










