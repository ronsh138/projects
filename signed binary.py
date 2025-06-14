num = int(input("number: "))
num_of_bits = int(input("number of bits the number will be represented by: "))
max_num = 0
for i in range(num_of_bits):
    max_num += pow(2, i)

neg_num = num^max_num
neg_num += 1

print(bin(neg_num))