def percentage():
    print('                                                                LETS CALCULATE YOUR PERCENTAGE')
    eng=int(input('ENTER YOUR ENGLISH MARKS:'))
    if eng>80:
        print('WRONG MARKS.USE THE MARKS THAT U GOT OUT OF 80')
        print('PLEASE TRY AGAIN!!!!!')
        return

    maths=int(input('ENTER YOUR MATHS MARKS:'))
    if maths>80:
        print('WRONG MARKS.USE THE MARKS THAT U GOT OUT OF 80')
        print('PLEASE TRY AGAIN!!!!!')
        return
    
    science=int(input('ENTER YOUR SCIENCE MARKS:'))
    if science>80:
        print('WRONG MARKS.USE THE MARKS THAT U GOT OUT OF 80')
        print('PLEASE TRY AGAIN!!!!!')
        return

    hindi=int(input('ENTER YOUR HINDI MARKS:'))
    if hindi>80:
        print('WRONG MARKS.USE THE MARKS THAT U GOT OUT OF 80')
        print('PLEASE TRY AGAIN!!!!!')
        return

    social_science=int(input('ENTER YOUR SST MARKS'))
    if social_science>80:
        print('WRONG MARKS.USE THE MARKS THAT U GOT OUT OF 80')
        print('PLEASE TRY AGAIN!!!!!')
        return

    else :
        z=eng+science+maths+hindi+social_science
        print('SO,YOUR TOTAL MAKRS WITHOUT ASSESMENT ARE:',z)
        print('   ')
        print('20 MARKS WILL BE ADDED TO ALL THE SUBJECTS BECAUSE OF ASSESMENT:-')
        print('       ')
        eng2=eng+20
        print('YOUR NEW ENGLISH MARKS ARE:',eng2)
        maths2=maths+20
        print('YOUR NEW MATHS AMRKS ARE:',maths2)
        science2=science+20
        print('YOUR NEW SCIENCE MARKS ARE:',science2)
        hindi2=hindi+20
        print('YOUR NEW HINDI MARKS ARE:',hindi2)
        social_science2=social_science+20
        print('YOUR NEW SST MARKS ARE',social_science2)
        print('   ')
        y=eng2+science2+maths2+hindi2+social_science2
        print('   ')
        print('SO, YOUR NEW TOTAL ARE:',y)
        print('   ')
        print('YOUR TOTAL PERCENTAGE WITHOUT ASSESMENT IS:',z/500*100)
        print('YOUR TOTAL PERCENTAGE WITH ASSESMENT WILL BE:',y/500*100)
percentage()
