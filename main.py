print('Hello there welcome to the customer service chatbot')
print('   ')
user_name = input('What is your name? ')
user_age = input('What is your age? ')
print('  ')
print('How may I help you.')

def menu():
  print('1: place holder')
  print('2: place holder')
  print('3: place holder')
  print('4: place holder')
  print('0: exit')

menu()
user_choice = int(input('please select the field that pertains to you: '))

while user_choice != 0:
  if user_choice == 1:
    print()
    user_choice = input('Have you tried ... ')
    if user_choice == 'yes':
      user_choice = input('Have you tried ... ')
      if user_choice == 'yes':
        user_choice = input('Have you tried ... ')
        if user_choice == 'yes':
          print('Im sorry I couldnt help please call tech support instead')
          user_choice = 0
        elif user_choice == 'no':
          print('try that and come back again')
        else:
          print('Im sorry that isnt an option try typing yes or no')
      elif user_choice == 'no':
        print('try that and come back again')
      else:
        print('Sorry that isnt an option try typing yes or no')
    elif user_choice == 'no':
      print('try that and then come back')
    else:
      print('Im sorry that isnt an option please type yes or no')
  elif user_choice == 2:
    print()
    print('2')
  elif user_choice == 3:
    print()
    print('3')
  elif user_choice == 4:
    print()
    print('4')
  else:
    print()
    print('invalid option')

  print()
  menu()
  user_choice = int(input('please select the field that pertains to you: '))

print()
print('Thank you for  using customer service chatbot!')