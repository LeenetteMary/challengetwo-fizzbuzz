list1 = [1,2,3,4,2]
list2 = [1,3,4,3]

def fizzbuzz(n,m):

    new_list = len(n) + len(m)

    if new_list % 3 == 0:
        return print('Fizz')
    elif new_list % 5 == 0:
        return print('buzz')
    elif new_list % 5 == 0 and new_list % 3 == 0:
        return  print('fizzbuzz')
    else:
        return  print('not divisible by both')
        
fizzbuzz(list1,list2)