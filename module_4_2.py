def test_function():
	def inner_function():
		print("Я в области видимости функции test_function")
	inner_function()

test_function()

#при вызове inner_function вне функции test_function выходит ошибка NameError: name 'inner_function' is not defined