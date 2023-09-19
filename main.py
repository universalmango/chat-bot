print('Hello there welcome to the customer service chatbot')
print('   ')
user_name = input('What is your name? ')
user_age = input('What is your age? ')
print('  ')
print('How may I help you.')

def menu():
  print('1: My device isnt working')
  print('2: I cant find an item')
  print('3: Im reporting an incident')
  print('0: exit')

def second_menu():
  print('1: an employee was not doing their job')
  print('2: an employee is being harassed')
  print('3: a customer is being harassed')
  print('4: there is a fight')
  print('5: there is a thief')
  print('0: exit')

menu()
user_choice = int(input('please select the field that pertains to you: '))
where = 0
confirm = 0

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
    second_menu()
    user_choice = int(input('Select the field that applies: '))

    while True:
      if user_choice == 1:
        print()
        employee_badge = int(input('Please input employee badge number: '))
        print('Thank you for telling us about this issue!')
        break
      elif user_choice == 2:
        print()
        print('please tell us where this happened')
        where = input('please say the isle or chekout then the number exmp: isle 1: ')
        break
      elif user_choice == 3:
        print()
        print('please tell us where this happened ')
        where = input('please say the isle or chekout then the number exmp: isle 1: ')
        break
      elif user_choice == 4:
        print()
        print('please tell us where this is happening ')
        where = input('please say the isle or chekout then the number exmp: isle 1: ')
        break
      elif user_choice == 5:
        print()
        print('please tell us what the thief is wearing and what clothes they have on')
        who = input('If you have it please also tell us the license plate number: ')
        break
      elif user_choice == 0:
        break
      else:
        print('Sorry that isnt an option')
  else:
    print()
    print('invalid option')

  while True:
    print()
    confirm = input('is that all? (yes, or no) ')
    if confirm == 'yes':
      user_choice = 0
      break
    elif confirm == 'no':
      user_choice = 1
      break
    else:
      print('Im sorry that isnt an option try typing yes or no in all lowercase')
        
  if user_choice != 0:
    print()
    menu()
    user_choice = int(input('please select the field that pertains to you: '))
  
print()
print('Thank you for our customer service bot! ' + user_name)