# Откройте текстовый файл task3.txt для чтения.
# Извлеките все уникальные слова из файла (слова разделяются пробелами и знаками пунктуации).
# Подсчитайте, сколько раз каждое уникальное слово встречается в тексте.
# Запишите результаты в новый файл в формате:
# слово1: количество
# слово2: количество
#
# Убедитесь, что слова записаны в алфавитном порядке.
f=open("task3.txt",encoding="utf-8")
f=f.read()
f=f.lower()
a=f.split()
b=[]
for i in range(len(a)):
    if a[i]!="—" and a[i]!="*" and a[i]!='-':
        b.append(a[i])
c=[]
for i in range(len(b)):
    par=True
    if b[i][-1]==',' or b[i][-1]==".":
        b[i]=b[i][0:len(b[i])-1]
    b[i]=b[i].lower()
    for j in range(len(c)):
        if b[i]==c[j]:
            par=False
    if par:
        c.append(b[i])
c.sort()

for i in range(len(a)):
    if a[i][-1]==',' or a[i][-1]==".":
        a[i]=a[i][0:len(a[i])-1]
for i in range(len(c)):
    print(c[i]," ", a.count(c[i]))
