import os

def rename():
      print('Changing file names...')
      files = [f for f in os.listdir('.') if os.path.isfile(f)]
      i = 0
      
      for file in files:
            if not file.endswith('.py'):
                  i = i + 1
                  name = os.path.splitext(file)[0]
                  extension = os.path.splitext(file)[1]
                  os.rename(file, str(i) + extension)
                  
      print('Renaming is done!!!')     
      x = input('Press enter to close program:' )

def rename1():
      files = [f for f in os.listdir('.') if os.path.isfile(f)]

      #might change
      i = 10000
      
      for file in files:
            if not file.endswith('.py'):
                  i = i + 1
                  name = os.path.splitext(file)[0]
                  extension = os.path.splitext(file)[1]
                  os.rename(file, str(i) + extension)
                  

#main function
print('\n ---------------')
print('| 1)Rename File |\n| 2)Cancel      |')
print(' ---------------')
option = input('Select an option: ')
while option != '1' and option != '2':
      os.system('cls')
      option = input('Invalid input, Please enter again: ')
      
if option == '1':
      os.system('cls')
      rename1()
      rename()
      

