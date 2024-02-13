from random import *

## completed for you, use as a template
def get_positive_answer(answer):
    ans = "You may rely on it."
    if answer == 0:
        ans = "As I see it, yes."
    elif answer == 1:
        ans = "Signs point to yes."
    elif answer == 2:
        ans ="Outlook good."
    elif answer == 3:
        ans = "Without a doubt."
    return ans
    
## Uncomment, and add your own - then remove when done. 
#print("TESTING", get_positive_answer(1))
#print("TESTING", get_positive_answer(3))
#print("TESTING", get_positive_answer(4))

def get_negative_answer(answer):
    ans = ""
    if answer == 0:
        ans = "Don’t count on it."
    elif answer == 1:
        ans = "My reply is no."
    elif answer == 2:
        ans = "My sources say no."
    elif answer == 3:
        ans = "Outlook not so good."
    elif answer >= 4:
        ans = "Very doubtful."
    return ans
    return ans
    
## Uncomment, and add your own - then remove when done. 
#print("TESTING", get_negative_answer(1))
#print("TESTING", get_negative_answer(2))
#print("TESTING", get_negative_answer(3))
#print("TESTING", get_negative_answer(4))

def get_no_answer(answer):
    ans = ""
    if answer == 0:
        ans = "Reply hazy, try again."
    elif answer == 1:
        ans = "Ask again later."
    elif answer == 2:
        ans = "Better not tell you now."
    elif answer == 3:
        ans = "Cannot predict now."
    elif answer >= 4:
        ans = "Concentrate and ask again."
    return ans
    return  ans
    
## Uncomment, and add your own - then remove when done. 
#print("TESTING", get_no_answer(1))
#print("TESTING", get_no_answer(2))
#print("TESTING", get_no_answer(3))
#print("TESTING", get_no_answer(4))


def get_answer(category, answer):
    ans = None
    if category < 24:
        return get_negative_answer(answer)
    elif 24 <= category <= 73:
        return get_no_answer(answer)
    else:
        return get_positive_answer(answer)
    return ans
    
## Uncomment, and add your own - then remove when done. 
#print("TESTING", get_answer(74, 3))
#print("TESTING", get_answer(75, 2))
#print("TESTING", get_answer(25, 1))
#print("TESTING", get_answer(5, 1))

def printSplash(): ## you should change this for fun and playing with strings
    print('88888888888888888888')
    print('8   Magic 8 Ball   8')
    print('8    Ask away      8')
    print('88888888888888888888')


# This method 'runs' the program. You can assume it is correct, but we encourage you to look
# through he code. Notice the randint - that gives you a random number between 0 and 99
def run():
    cat = randint(0, 100)
    an = randint(0, 4)
    print(f'category num: {cat} answer num:  {an}')
    print(get_answer(cat, an))
    print()
    user_input = input('Ask another question (Yes/No?): ')
    if user_input.lower().startswith('n'):
        print('Thank you for playing!')
        return
    print('\nAnd the answer is...\n') 

if __name__ == '__main__':
    printSplash()
    run()

