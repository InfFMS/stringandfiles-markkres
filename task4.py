# Напишите программу, которая просит пользователя ввести несколько предложений (например, 5, каждое предложение с новой строки).
# Каждое введенное предложение записывается в файл, но:
# Слова во всех предложениях должны быть приведены к верхнему регистру.
# Между словами вместо пробела ставится символ "_".
# После записи откройте этот файл, считайте содержимое и выведите его на экран.
N=int(input("количество строк: "))
mas=[]
for i in range(N):
    file = open("For_task4.txt", "w")
    string=input()
    string=string.upper()
    #print(string)
    string = string.replace(" ","_")
    #print(string)
    mas.append(string)
string="\n".join(mas)
file.write(string)
file.close()
f=open("For_task4.txt","r")
f=f.read()
print(f)
