#The Fibonacci Sequence
first_num = int(0) # initiate the first number to be zero
n=7 # since the first number is defined, setting the sequence number to 7
x=int(1) #initialize
snd_num = input("Enter your second number:") # accept user input for the second number
while x <=n: # loop until n = 7
 if x<=1:
   print(first_num) # print the 1st num
   print(snd_num)  # print the 2nd number
   x=x+1 # increment x
 elif x > 1:
  new_num = int(first_num) + int(snd_num) # get the next number
  print(new_num) #print the next number
  first_num = snd_num  # assign 2nd number to be first number
  snd_num = new_num # assign new number to be 2nd
  x = x + 1 # increment x
 

 
 