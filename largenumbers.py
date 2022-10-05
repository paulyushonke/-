import random
import time

power = int(input("enter a key length: "))
result = 2**power
print(f"the number of key variants that can be specified by a {power}-bit sequence is {result}")

gen_num = random.randint(0, result-1)
print(f"your random key:{gen_num}")
start_time = time.time()
while True:
     num2 = random.randint(0, result-1)
     if num2 == gen_num:
        break

print(f"%s miliseconds to find a value {num2} equal to the previously generated key" % ((time.time() - start_time)*1000))
