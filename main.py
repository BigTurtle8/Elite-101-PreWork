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

if __name__ == '__main__':
  print('Elite101 Chatbot')
  print('')
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

  print(getMessage(name, age))  
