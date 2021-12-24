def decode(func):
   def wrapper(message):
      # Sorting the message after being cleaned
      message = sorted(func(message))
      for index in range(0, len(message)):
         n = 0-(int(message[index])-9) # Mapping numbers to their actual values
         message[index] = str(n)
      s = ""
      return s.join(message)
   return wrapper

@decode
def clean_message(message):
   # Removing every character that's not digit
   cleaned = [character for character in message if character.isdigit()]
   return cleaned
