def getUserInfo():
  name = input('Hello! I am a chatbot designed to help you. What is your name? ')
  
  while True:
    try:
      age = int(input('Welcome ' + name + '! How old are you? '))
    except ValueError:
      print('Sorry, that is not a valid age. Please enter a whole number.')
      continue
    else:
      if age < 0:
        print('Sorry, that is not a valid age. Please enter a positive number (or 0).')
        continue
      else:
        break
  
  return name, age

def getMessage(name, age):
  if age < 15:
    return 'Hello little one! How can I help you, ' + name + '?'
  elif 15 <= age and age < 18:
    return 'Hello! How can I help a young adult like yourself, ' + name + '?'
  elif 18 <= age and age < 55:
    return 'Hello! How can I be of assistance to you, ' + name + '?'
  elif 55 <= age and age < 120:
    return 'Hey, I remember when I was that young! How can I help, ' + name + '?'
  elif age >= 120:
    return 'Well, I hope I live to your age! How can I help, ' + name + '?'

def printConversationMenu():
  print('Select one of the following options: ')
  print('1. Placeholder 1')
  print('2. Placeholder 2')
  print('3. Placeholder 3')
  print('4. Exit')

def getConversationChoice():
  # newline for style
  print()
  printConversationMenu()
  return input('Please enter the number of your chosen option: ')

def printErrorMessage():
  print()
  print('I am sorry, but that is not a valid option. ' +
        'Type \'1\', \'2\', \'3\', or \'4\' to select an option.')

def printConversationMessage(option):
  # newline for styling
  print()
  print(getConversationMessage(option))

def getConversationMessage(option):
  if option == '1':
    return 'Placeholder 1 Response'
    
  elif option == '2':
    return 'Placeholder 2 Response'
    
  elif option == '3':
    return 'Placeholder 3 Response'

  return None

def printContinueMessage(name):
  print()
  print('Is there anything else you would like help with, ' + name + '?')

def printExitMessage(name):
  print()
  print(' <> I hope I was helpful, ' + name + '. Goodbye! <>')

if __name__ == '__main__':
  print('Elite101 Chatbot')
  print()

  name, age = getUserInfo()

  print(getMessage(name, age))  

  while True:
    option = getConversationChoice()
  
    while option not in [str(x) for x in range(1, 5)]:
      printErrorMessage()
      
      option = getConversationChoice()
  
    if option == '4':
      printExitMessage(name)
      break

    printConversationMessage(option)

    printContinueMessage(name)

#this is a test modification