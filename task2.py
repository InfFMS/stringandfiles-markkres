# Откройте текстовый файл task2.txt для чтения.
# Считайте его содержимое в строку.
# Найдите и замените все вхождения слова "Python" на слово "Питон" (регистр учитывать).
# Запишите обновленный текст в новый файл с другим именем.
# Выведите на экран сообщение о количестве произведённых замен.
f=open("task2.txt",encoding="utf-8")
string=f.read()
string=string.replace("Python","Питон")
string=string.replace("python","питон")
file = open("For_task2.txt","w+")
file.write(string)
file.close()
