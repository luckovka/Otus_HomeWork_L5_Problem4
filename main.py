import pandas as pd

customers_dict = dict()
while customer := input("Введите данные пользователя через пробел: "):
    name, last_name, age, id = customer.split()

    if len(id) < 8:
        id_list = list(id)
        while len(id_list) < 8:
            id_list.append("0")
        id = "".join(id_list)
    customers_dict[id] = (name, last_name, age)

    if not name.istitle():
        name = name.capitalize()
    if not last_name.istitle():
        last_name = last_name.capitalize()

    customers_dict[id] = (name, last_name, age)
    try:
        if int(id):
            id = id
    except:
        if ValueError:
            customers_dict.popitem()
            print("ID введен некорректно, повторите попытку: ")
    if int(age) >= 18 and int(age) <= 60:
        age = age
    else:
        print("Возраст пользователя должен быть от 18 до 60 лет")
        customers_dict.popitem()
    if not name.isalpha() or not last_name.isalpha():
        print("Имя и фамилия пользователя должны содержать только буквы")
        customers_dict.popitem()

keys_list = list(customers_dict.keys())
values_list = list(customers_dict.values())
columns_name = ["ИМЯ", "ФАМИЛИЯ", "ВОЗРАСТ"]

customers_df = pd.DataFrame(values_list, columns=columns_name, index=keys_list)
print(customers_df)