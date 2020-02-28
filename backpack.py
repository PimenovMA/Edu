# -*- coding:utf-8 -*-
""" 
Программа показывающая работу класса на примере объекта Bacpack (Рюкзак)
"""
class Рюкзак:
	# в __init__ записываем все переменные класса
	def __init__(self, подарок = None):
		
		# создаем пустой одномерный массив (список) content
		# слово "self" для организации взаимодействия перменных внутри класса
		self.content = []
		""" 
		проверяем, если есть подарок, записываем его в рюкзак
		т.е. ложим его в массив content
		"""
		if подарок is not None:
			self.content.append(подарок)
	
	# создаем метод добавления в рюкзак (в массив)		
	def add (self, добавка):
		self.content.append(добавка)
	
	# созадем метод вывода содержимго рюкзака (массива)
	def inspect (self, item):
		print(u"В рюкзаке лежит:")
		# в цикле выводим содержимое списка (массива)
		for item in self.content:
			print ('    ',item)


# создаем объект типа Рюкзак() с подарком
рюкзак = Рюкзак('Флешка')

print ('"выход" для выхода')
ввод_данных = ''
# Вводим данные в цикле
while ввод_данных != 'выход':
	ввод_данных = input ('Что ложим в Рюкзак? ')
	# Задаем условие для выхода из цикла
	if ввод_данных == 'выход' or ввод_данных == 'Выход': 
		break
	# Запихиваем введенные данные в рюкзак
	рюкзак.add (ввод_данных)

# выводим содержимое рюкзака	
рюкзак.inspect(ввод_данных)

