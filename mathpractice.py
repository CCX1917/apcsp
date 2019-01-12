#Math Practice

#To begin, type in the practtice function. It is a very simple test of Algebra.

def practice():
    print('We are going to do an algebra problem')
    print('If 3x = 6, then what does x equal?')
    answer= int(raw_input())
    if answer == 2:
        print('Yes! You got it right! You can do Algebra problems!')
    else:
        print('Nope, sorry')
        print('Here is another one. See if you can get it right this time.')
        print('If 10 + x = 20, then what does x equal?')
        answer2= int(raw_input())
        if answer2 == 10:
            print('Yes! You learned Algebra!')
        else:
            print('Sorry. You will have to review how to do Algebra')