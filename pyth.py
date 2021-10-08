def function (n, system):
	result = ""
	while n > 0:
		result += str (n % system)
		n //= system
	return result[::-1]

n = int (input ("Любое число: "))
system = int (input ("Целевая система счисления, в которую переводить число: "))
notation_list = [2, 8]
if system in notation_list:
	if n >= 0:
		print (str (n) + " -> " + str (function (n, system)))
	elif number == 0:
		print ("0 -> 0")
else:
	print ("Действие невозможно!")