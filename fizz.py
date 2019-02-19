input_list1 = input('enter values of list1: ')
input_list2 = input('enter values of list2: ')

list1 = input_list1.split()
list2 = input_list2.split()

new_list = len(list1) + len(list2)

def fizz(a,b):

    if new_list % 3 == 0:
        return print('Fizz')
    elif new_list % 5 == 0:
        return print('buzz')
    elif new_list % 5 == 0 and new_list % 3 == 0:
        return  print('fizzbuzz')
    else:
        return  print('not divisible by both')
        
fizz(list1,list2)
