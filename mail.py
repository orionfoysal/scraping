# import re
# def isValidEmail(email):
#     if len(email) > 7:
#         if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
#             return True
#     return False

# if isValidEmail("my.email@gmail.com") == True :
#     print("This is a valid email address")
# else:
#     print("This is not a valid email address")


import re

addressToVerify =''
match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{3})$', addressToVerify)

# if match == None:
# 	print('Bad Syntax')
# 	raise ValueError('Bad Syntax')

if match != None:
    print('Good')