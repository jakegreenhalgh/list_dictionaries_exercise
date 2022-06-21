# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
for num in numbers:
    if num % 2 == 0:
        print(num)

# 2. Print the difference between the largest and smallest value:
print(max(numbers)-min(numbers))

# 3. Print True if the list contains a 2 next to a 2 somewhere.
i = 0
for num in numbers:
    if num == 2 and numbers[i+1] == 2:
        print('true')
    i = i + 1

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

total = 0
count = True
for x in numbers:
  if x == 6:
    count = False
  if count:
    total += x
  if x == 7:
    count = True
print (total)


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

total = 0
off_count=2
for y in numbers:
    if y == 13:
        off_count=0
    if off_count >= 2:
        total+=y
    off_count+=1
print (total)






