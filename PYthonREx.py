import re 

regex = r'\b[A-Za-z0-9._%+-]+@gmail+\.[com|edu]'
email = input('Your Email Please !!!\n')
if(re.search(regex, email)):
    print("Valid Email")
else:
    print("Invalid Email")