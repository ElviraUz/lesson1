#Урок: Функции
#Задание1
def get_summ (one, two, delimiter='&'):
  one=str(one)
  two=str(two)
  delimiter= str(delimiter)
  return (one+delimiter+two)
sentence = get_summ("Learn", "Python")
p = sentence
print(p.upper())

#Задание2
def format_price (price):
    price = int(price)
    return f"Цена: {price} руб."

z=format_price (56.24)
print(z)
