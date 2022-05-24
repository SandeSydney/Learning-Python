#Prompting for User Input

greeting = input('What is your name? ')

#display the inputted text
print('Hello there {}'.format(greeting))

#Greeting response
response = input('How are you?')

#if-else with the answer
if response in ("Good", "good", "Great", "great", "OK", "Ok", "ok"):
   print('Am glad to hear that {}'.format(greeting))
else:
   print('So sad {}. I hope your day improves'.format(greeting))
