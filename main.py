print('Hello there welcome to the customer service chatbot')
print('   ')
user_name = input('What is your name? ')
user_age = input('What is your age? ')
print('  ')
print('How may I help you.')

def menu():
  print('1: My device isnt working')
  print('2: I cant find an item')
  print('3: place holder')
  print('4: place holder')
  print('0: exit')

menu()
user_choice = int(input('please select the field that pertains to you: '))

while user_choice != 0:
  if user_choice == 1:
    while user_choice != 0:
      print()
      user_choice = input('Have you tried ... ')
      if user_choice == 'yes':
        print()
        user_choice = input('Have you tried ... ')
        if user_choice == 'yes':
          print()
          user_choice = input('Have you tried ... ')
          if user_choice == 'yes':
            print()
            print('Im sorry I couldnt help please call tech support instead')
            user_choice = 0
          elif user_choice == 'no':
            print()
            print('try that and come back again')
            user_choice = 0
          else:
            print()
            print('Im sorry that isnt an option try typing yes or no')
        elif user_choice == 'no':
          print()
          print('try that and come back again')
          user_choice = 0
        else:
          print()
          print('Sorry that isnt an option try typing yes or no')
      elif user_choice == 'no':
        print()
        print('try that and then come back')
        user_choice = 0
      else:
        print()
        print('Im sorry that isnt an option please type yes or no')
  elif user_choice == 2:
    print()
    user_choice = input('What item are you having trouble finding? ')
    print('the item you want help with is: ' + user_choice)
    user_choice = input('Is this correct| yes , no: ')
    while user_choice == 'no':
      user_choice = input('Sorry. please type in the item you are looking for: ')
      print('is this the item you are looking for: ' + user_choice)
      user_choice = input('yes , no: ')
    if user_choice == 'yes':
      print('please wait for an employee to come help you find your item')
      user_choice = 0
  elif user_choice == 3:
    print()
    print('3')
  elif user_choice == 4:
    print()
    print('4')
  else:
    print()
    print('invalid option')

  if user_choice != 0:
    print()
    menu()
    user_choice = int(input('please select the field that pertains to you: '))
  
print()
print('Thank you for our customer service bot! ' + user_name)