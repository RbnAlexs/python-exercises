print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
mixed_name = str(name1) + str(name2)
mixed_name = mixed_name.lower()
true_count = love_count = 0
true_list = ['t','r','u','e']
love_list = ['l','o','v','e']
for i in mixed_name:
  #print(i)
  true_count += true_list.count(i)
  love_count += love_list.count(i)
result = int( str(true_count) + str(love_count) )
if (result  < 10) or (result > 90):
  print(f"Your score is {result}, you go together like coke and mentos.")
elif (result >= 40) and (result <=50):
  print(f"Your score is {result}, you are alright together.")
else:
  print(f"Your score is {result}.")