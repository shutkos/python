# Одночасна обробка кількох словників
# 1/1 бал (оцінюється)
# Дані:
# stock = {
#    'banana': 6,
#    'apple': 0,
#    'orange': 32,
#    'pear': 15
#   }
# prices = {
#    'banana': 4,
#    'apple': 2,
#    'orange': 1.5,
#    'pear': 3
#   }
# Створіть програму, яка рахує загальну вартість з використанням словників stock і prices, а потім друкує результат.
stock = {
   'banana': 6,
   'apple': 0,
   'orange': 32,
   'pear': 15
  }
prices = {
   'banana': 4,
   'apple': 2,
   'orange': 1.5,
   'pear': 3
  }
# write your program here
total = {k: stock[k] * prices[k] if k in stock.keys() and prices.keys() else 0 for k in prices}
a = sum(total.values())
print(a)