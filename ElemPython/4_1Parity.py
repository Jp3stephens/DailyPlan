#How would you compute the parity of a very large number of 64-bit words? 

#Brute force solution

def parity(x: int) -> int: 
	result = 0
	while x: 
		result ^= x & 1
		x  >>= 1
	return result

#Brute force solution is O(n) where n is the word size

#First improvement is based on erasing the lowest set bit in a word in a single operation, thereby improving performance in the best and average cases. 
#bit fiddling trick: x&(x-1) equals x with its lowest set bit erased. 
#Ex: if x = (00101100) then x - 1 = (00101011) so x&(x-1) = (00101100)&(00101011 = (00101000). This fact can be used to reduce the time complexity. 
#Let k be the number of bits set to 1 in a particular word. Then time complexity of the algorithm below is O(k)

def parity2(x: int) -> int: 
	result = 0
	while x: 
		result ^= 1
		x &= x - 1 #Drops the lowest set bit of x
	return result
 
