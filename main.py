if __name__ == '__main__':
  print('Elite101 Chatbot')
  print('')
  name = input('Welcome! I am a chatbot designed to help you. What is your name? ')
  
  while True:
    try:
      age = int(input('Hello there ' + name + '! How old are you? '))
    except ValueError:
      print('Sorry, that is not a valid age. Please enter a whole number.')
      continue
    else:
      if age < 0:
        print('Sorry, that is not a valid age. Please enter a positive number (or 0).')
        continue
      else:
        break