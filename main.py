import os, random, string


print('\u001b[32mWelcome to Offline Password Generator.\nTo stop at any point just press CTL+C, Automatic Proccess will generate a password of 18 that includes letters, numbers and special characters !@#$%^&*(). With Manual Process you can customize everything')

autoKeys = ['auto', 'automatic', 'a']
mKeys = ['m', 'manual', 'man'] 
auto = input ('\u001b[0m'+'Automatic Process or Manual? a/m: ') 

if auto.lower() in autoKeys:
    length = 18
    included = string.ascii_letters + string.digits + '!@#$%^&*()'
    random.seed = (os.urandom(2048))
    print ('\u001b[37;1mHere is your password:\u001b[32;1m',''.join(random.choice(included) for i in range(length)))
    print('\u001b[34;1mThanks for Using the Offile Password Generator. https://github.com/Abdessalamm/offline-passwd-generator'+'\u001b[0m')
  
elif auto.lower() in mKeys:  
 length = input ('Length of the password? Default is: 18: ')

 if length == '0' or not length:
    length = '18'
     
 splcar = input('What special characters to include? like !@#$%^&*() leave empty if none: ')
 yKeys = ['y', 'Y', 'Yes', 'YES', 'yes']
 letters = input('Include letters? Yes/No: ')
 nums = input ('Include Numbers? Yes/No: ')

 if letters in yKeys or not letters:
    ltr = string.ascii_letters
 else:
    ltr = ''  
    
 if nums in yKeys or not nums:
    num = string.digits
 else:
    num = ''      
 included = ltr + num + splcar
 random.seed = (os.urandom(2048))
 print ('\u001b[37;1mHere is your password:\u001b[32;1m', ''.join(random.choice(included) for i in range(int(length))))
 print('\u001b[34;1mThanks for Using the Offile Password Generator. https://github.com/Abdessalamm/offline-passwd-generator'+'\u001b[0m')
 
else:
    print('\u001b[31m'+'Please restart the app and type only a or m | a for automatic or m for manual.')
