def check_prime(number):
    for i in range(2, int((number/2) + 1)):
        if number % i == 0:
           return False
        else:
           return True
    if number == 1:
        return False
    else:
        return True
       

N = 10
num = 1
output_list = []
while N != len(output_list):
    if check_prime(num):
        output_list.append(num)
    num += 1
    
print(output_list)
    