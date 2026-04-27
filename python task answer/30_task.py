def print_bill(*args ,**kwargs):
	
	for item in args:
		print(f"-{item}")
	
	total =0
	print ("-"*20)
	for item, price in kwargs.items():
		print(item,"=",price)
		
		total +=price
	print ("-"*20)
	print("Total Bill:", total)

print_bill("bilu chaiwala","yaha sare Tarah ki chai milti hai",chai=5,full_cup=10, biscut=10)