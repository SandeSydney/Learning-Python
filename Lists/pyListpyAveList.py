## This file contains code that finds the average of numbers that are keyed into a list

num_list = list()
while True:
    txt_input = input('Key in the number you\'d like. Type "done" to complete: ')
    if txt_input == 'done': break  
    num = float(txt_input)
    num_list.append(num)

average = (sum(num_list)/len(num_list))
print('Your average: ', average)