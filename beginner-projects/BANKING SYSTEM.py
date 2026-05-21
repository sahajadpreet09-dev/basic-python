print('                                                                             WELCOME!!!!')
print('                                                                          to digital bank!')
total=int(input('how much money do u currently have in your bank account'))
print('OKAY, so would u like to do ')
state=input('deposit OR withdraw')
if state == 'deposit':
    addition=int(input('HOW MUCH WOULD U LIKE TO DEPOSIT'))
    print('SO YOUR NEW TOTAL IS',total+addition,'rs')
else:
    negative=int(input('HOW MUCH WOULD U LIKE TO WITHDRAW'))
    print('SO YOUR NEW TOTAL IS',total-negative,'rs')

    
 
