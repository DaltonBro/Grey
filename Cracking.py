# Brute force, check all 1 charactes, then all 2 characters and so on
# python3 Cracking.py 
#
#


Password = input("What is your Password: ")
Passlist = list(Password)
print(Passlist)

s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
Check = [0]
			
				
				
def cycle():
	x=0
	while (x < 63):
	
		Check[len(Check)-1] = s[x]  		 ##last part of list
		
		print(Check)
		if(Check == Passlist):    		##check if the list matches
			quit()
							
		if(x == 61):	 			##at last character of list
			Allvalue = 0
			for t in range(0,len(Check)):
				Allvalue = Allvalue + s.index(Check[t])		##total value of all positions
			if(Allvalue == 61*(len(Check))):			##have we check all up to now
				Check.append(len(Check))       			 ##add another character
				for i in range(0,len(Check)):
					Check[i] = s[0]                 ##restart checks		
								
			elif(len(Check) > 2):                     ##if we have more then 2 characters
				for y in range(0,len(Check)-2): 		##check through each character in check
					if (Check[len(Check) -2 - y] == s[61]):		##is that character(except for last and first, at the end
						Check[len(Check) -2 -y] = s[0]		##turn that character back to the start
						Position = s.index(Check[len(Check) -3 -y]) 	#Find postion of character in check before
						Check[len(Check) -3 -y] = s[Position + 1]	#move the character one down
						Check[len(Check)-1] = s[0]			#stop it from double adding on the second before last
				if (Check[len(Check) - 1] != s[0]):
					Position = s.index(Check[len(Check)-2])		#Find first place position
					Check[len(Check)-2] = s[Position + 1]		#Move first postion up
				
			elif(len(Check) == 2):				#Are we at 2 characters
				Postion = s.index(Check[0])		#Find first place position
				Check[0] = s[Postion + 1]		#Move first postion up
				

			
			x = -1	
		x= x+1

			
while Check != Passlist:
	cycle()

