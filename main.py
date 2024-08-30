import random
def randomize(): # Randomize the numbers in the list
  list = []
  for i in range(1,101):
    list.append(i)
  random.shuffle(list)
  return list
success = 0 # counter to maintain how many successes we have
for i in range(1000): # n amount of trials.
  print(i)
  bool_list = []
  round = True
  list = randomize()
  # print(list)
  for j in range(1,101): # One round where each player does the thing # Each player gets a number
    k=1
    indiv_success = False
    while k <= 50: # They get 50 attempts to find their number
      guess = list[j-1]
      # print(j)
      # print(guess)
      if guess == j:
        indiv_success = True
        k=51
      elif guess != j:
        k=2
        while k <= 50:
          guess = list[guess-1]# If they don't find their number in their box, open the box that has that number on it.
          # print(str(k) + ':' + str(guess))
          if guess == j:
            indiv_success = True
          k+=1
      bool_list.append(indiv_success)
  try:
    bool_list.index(False) # This will work if we find something.
    print('Successes: ' + str(success))
  except: 
    success +=1 # If there's no false, the prisoners succeeded!
    print('Successes: ' + str(success))