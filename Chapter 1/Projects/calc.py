#las siguientes son las funciones de cada operacion
def suma(one, other):
	return float(one) + float(other)
def resta(one, other):
	return float(one) - float(other)
def mult(one, other):
	return float(one) * float(other)
def div(one, other):
	return float(one) / float(other)
def pot(one, other):
	return float(one) ** float(other)


def oper_order(opers):  #Función que ordena los operadores usados, basandose en la precedencia de operadores (primero la potenciación, después la multiplicación o división y por último la suma y resta, que, al ser consideradas iguales, se ordenan según como estaban ubicadas)
	real_ord = []  #lista final del orden de operadores
	for i in opers:
		if i == '**':
			real_ord.append(i)
			opers.remove(i) 
	for i in opers:	
		if i in '*/':  #si el operador es / o *
			real_ord.append(i)
			opers.remove(i)
	for i in opers:
		real_ord.append(i) #se agregan el + y el - en el order en el q estaban (de izq a der)
	return real_ord
	
	
def finish_parentesis(a, ans):
	between = a[a.index('(')+1 : 0 -(a[::-1].index(')')+1) ]
	solved_parentesis = str(start(between, ans))
	final = a.replace(f'({between})', solved_parentesis)
	return separate_input(final, ans)
	

def answering(num, ans):
	if num == "ans":
		return str(ans)
	else:
		return num
	
	
def separate_input(text, ans):
	values = []
	pot_counter = False
	num =""
	if '(' in text:
		return finish_parentesis(text, ans)
	for i in text:
		if i in "+-/**":
			if not num and i in "+-":
				num += i
			elif pot_counter and i == '*':
				values.append('**')
				pot_counter = False
			elif not pot_counter and i == '*':
				values.append(answering(num, ans))
				pot_counter = True
				num = ''
			elif pot_counter and i != '*':
				values.append('*')
				pot_counter = False
				num += i
			else:
				values.append(answering(num, ans))
				values.append(i)
				num = ""
		else:
			if pot_counter:
				values.append('*')
				pot_counter = False
				num += i
			else:
				num += i
	values.append(answering(num, ans))
	return values	


def post_operation(abio):
	if abio != 0.0:
		if not abio % int(abio):
			return(int(abio))
		else:
			return(abio)
	else: return abio
			
			
def start(a, ans):
	try:
		if not a: return ''
		dict = {'+' : suma, '-' : resta, '*' : mult, '/' : div, '**' : pot}
		values = separate_input(a, ans)
		used = []
		for i in values:
			if i in dict:
				used.append(i)
		if not used:
			return post_operation(float(answering(a, ans)))
		used = oper_order(used)		
		for i in used:
			index = values.index(i)
			abio = dict[i](values[index-1], values[index+1])
			del values[index-1:index+2]
			values.insert(index-1, abio)
		return post_operation(abio)
	except ZeroDivisionError:
		return('Math Error')
	except OverflowError:
		return('Error, enormous number to represent')
	except:
		return('Sintax Error')
			

if __name__ == "__main__":
	ans = 0
	print("To exit the calculator write 'quit()\nThe unique word command is 'ans'")
	while True:
		a = input('>>> ')
		if a != 'quit()' and a:
			ans = start(a, ans)
			print(ans)
		elif not a:
			continue
		else: break
