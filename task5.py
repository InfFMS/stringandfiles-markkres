# Откройте текстовый файл task5.txt для чтения.
# Найдите самое длинное слово в тексте. Если таких слов несколько, выберите первое из них.
# Запишите это слово и его длину в новый файл в формате:
# Самое длинное слово: слово
# Его длина: длина
#
# Выведите это слово и длину в консоль.
file = open("task5.txt", "r",encoding="utf-8")
f=file.read()
f=" ".join(f.split("\n"))
f=" ".join(f.split("."))
f=" ".join(f.split("!"))
f=f.split()
maximum=0
slovo=""
for i in range(len(f)):
    if len(f[i])>maximum:
        maximum=len(f[i])
        slovo=f[i]
file = open("For_task5.txt", "w",encoding="utf-8")
string="Самое длинное слово: "+str(slovo)+"\n"+"Его длина: "+str(maximum)
file.write(string)
file.close()
print(slovo)
print(maximum)

