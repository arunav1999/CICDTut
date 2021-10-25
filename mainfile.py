
class MainFileCode:	
	def isPrime(self,n):
		if(n > 1):
			for i in range(2,(n//2) + 1):
				if((n % i) == 0):
					return (False,'Prime')
			else:
				return (True,'Prime')
		return (False,'Prime')

	def isPalindrome(self,string):
		for i in range(len(string)//2):
			if(string[i]!=string[len(string)-1 - i]):
				return (False,'Palin')
		return (True,'Palin')

	def isDecide(self,inp):
		if(inp.isnumeric()):
			return self.isPrime(int(inp))
		return self.isPalindrome(inp)

#Added a comment
#12
if __name__ == '__main__':
	inp = input()
	obj = MainFileCode()
	result = obj.isDecide(inp)
	if(result[1]=='Palin' and result[0]==False):
		print('The input is string and its not a Palindrome')
	elif(result[1]=='Palin' and result[0]==True):
		print('The input is string and its a Palindrome')
	elif(result[1]=='Prime' and result[0]==True):
		print('The input is integer and its a Prime number')
	elif(result[1]=='Prime' and result[0]==False):
		print('The input is integer and its a not a Prime number')