# Получаю от пользователя предложение в переменную типа строки
in_str = input("Введите предложение")
# создаю пустой результируюзий словарь
rez_dict = {}
# создаю лист слов разбивая полученную строку на слова через пробел
word_list = in_str.split(" ")
# перебираю в переменную word слова из листа слов
for word in word_list:
    # если в результирующем словаре нет ключа word
    if word not in rez_dict:
        # в результирующий словарь по ключу word записываю количество слов word в листе слов
        rez_dict[word] = word_list.count(word)

# вывожу получившийся словарь        
print(rez_dict)