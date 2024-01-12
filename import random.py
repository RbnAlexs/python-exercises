import random
import my_module

random_integer = random.randint(0,100)
print(my_module.pi)
print(random_integer)
random_decimal = random.random()
print(random_decimal)
#What is the range of random_decimal? 0.0000000000 to 0.9999999999
#What is the difference between randint and random? randint is inclusive of the last number, random is not
#What is the range of random_integer? 0 to 100

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
print(dirty_dozen[1][2])