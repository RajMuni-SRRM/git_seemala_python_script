class Ca:
	sum=0
	def __init__(self,no,sym,pre):
		self.no=no
		self.sym=sym
		self.pre=pre
		try:
			if self.sym=='+':
				self.sum=self.pre+self.no
				print('\t Result:',self.sum)
			elif self.sym=='-':
				self.sum=self.pre-self.no
				print('\t Result:',self.sum)
			elif self.sym=='*':
				self.sum=self.pre*self.no
				print('\t Result:',self.sum)
			elif self.sym=='/':
				self.sum=self.pre/self.no
				print('\t Result:',self.sum)
			else:
				print('\t Result:',self.sum)
		except ValueError as msg:
			print('enter numbers only',msg)
c=Ca(0,'+',0)
while True:
<<<<<<< HEAD
	try:
		if c.sum==0:
			no=int(input('enter the number:'))
			c=Ca(no,'+',0)
		else:
			sym=input('enter the operation:')
			no=int(input('enter the number:'))
			pre=c.sum
			c=Ca(no,sym,pre)
	except ValueError as msg:
		print('\t Result:',c.sum)
		print(msg)
		print('Thank you.....')
<<<<<<< HEAD
=======
		break
<<<<<<< HEAD
		
=======
>>>>>>> sprint2
<<<<<<< HEAD
>>>>>>> parent of 6081b2e... some change done in own caluclator
=======
        except ValueError as msg:
                print('\t Result:',c.sum)
                print(msg)
                print('Thank you.....')
                break

>>>>>>> sprint1
=======
	#try:
		#if c.sum==0:
			#no=int(input('enter the number:'))
			#c=Ca(no,'+',0)
		#else:
			#sym=input('enter the operation:')
			#no=int(input('enter the number:'))
			#pre=c.sum
			#c=Ca(no,sym,pre)
	#except ValueError as msg:
		#print('\t Result:',c.sum)
		#prinit(msg)
		#print('Thank you.....')
		#break
		
>>>>>>> b3a2700da452cc56f94ad41fdffe67d07e6f71fa
