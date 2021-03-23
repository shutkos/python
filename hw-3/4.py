# Напишіть програму, яка створює та друкує словник, використовуючи змінну sentence, де всі унікальні слова в
# sentence – ключі, а кількість згадок цих слів у sentence – значення. Всі ключі у словнику повинні бути в
# нижньому регістрі.
sentence = "Some random sentence"

sentence = sentence.split(' ')
sentence = {i.lower(): 1 for i in sentence}
print(sentence)