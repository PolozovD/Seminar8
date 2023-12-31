# print('Enter the first num: ')
# a = int(input())
# print('Enter the second num: ')
# b = int(input())
# print(f'{a} + {b} = {a + b}')


# print('Enter how many kilometers a car drives per day: ')
# n = int(input())
# print('Enter the number of kilometers you need to drive: ')
# m = int(input())

# print(f'You need {(m + n - 1) // n} days')


# print('Enter the number of desks in the first class: ')
# a = int(input())
# print('Enter the number of desks in the second class: ')
# b = int(input())
# print('Enter the number of desks in the third class: ')
# c = int(input())

# print(f'Minimum number of desks {(a + b + c + 1) // 2}')


# print('Введите номер вагона c головы поезда в который сел Витя: ')
# i = int(input())
# print('Введите номер вагона: ')
# j = int(input())

# if j < i or j > i:
#     print(f'В поезде {i + j - 1} вагонов')
# else:
#     print('Без дополнительной информации это сделать невозможно')


# print('Enter the year number: ')
# y = int(input())

# if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
#     print('YES')
# else:
#     print('NO')


# print('Enter the numbers of kilometers: ')
# n = int(input())
# print('Enter the numbers of kilometers you need to drive: ')
# m = int(input())
# print(f'You need {(m + n - 1) // n} days')


# print('enter the number of the sum of cranes: ')
# s = int(input())

# print(f'Peter, Kate, Serg made {s//6, s*2//3, s//6}')


# print('Enter a six-digit number: ')
# n = int(input())

# n1 = n // 1000
# n1Sum = n1 % 10 + n1 // 100 + n1 // 10 % 10
# n2 = n % 1000
# n2Sum = n2 % 10 + n2 // 100 + n2 // 10 % 10

# if n1Sum == n2Sum:
#         print(f'{n1Sum} == {n2Sum}, Yes, this is the lucky ticket!')
# else:
#         print(f'{n1Sum} != {n2Sum}, No, it''s not a lucky ticket')


# print('Enter n: ')
# n = int(input())
# print('Enter m: ')
# m = int(input())
# print('Enter k: ')
# k = int(input())

# if k % n == 0 or k % m == 0:
#     print('YES')
# else:
#     print('NO')


# print('Enter n: ')
# n = int(input())
# res = 1

# while n > 1:
#     res *= n
#     n -= 1
# print(res)  


# print('Enter a: ')
# a = int(input())
# res = 1
# fib = 0
# fib1 = 1
# fib2 = 0

# while fib <= a:
#     fib = fib1 + fib2
#     fib1, fib2 = fib, fib1
   
#     res += 1

# if (fib2 == a):
#     print(res)
# else:
#     print(-1)


# print('Enter number: ')
# n = int(input())



# n = 6
# numbers = "-20 30 -40 50 10 -10".split(" ")

# length = 0  # Текущая длина последовательности тёплых дней
# max_length = 0  # Максимальная длина последовательности тёплых дней

# for i in range(n):
#     el = int(numbers[i])

#     if el > 0:
#         length += 1
#     else:
#         length = 0

#     if length > max_length:
#         max_length = length

# print(max_length)



# n = 5
# numbers = "5 1 6 5 15".split(" ")

# min_weight = 1 
# max_weight = 1

# for i in range(n):
#     mas = int(numbers[i])

#     if mas <= min_weight:
#         min_weight = mas
#     elif mas >= max_weight: 
#         max_weight = mas
#     else:
#         pass

# print(min_weight, max_weight)



# from random import randint

# print('enter n: ')
# n = int(input())
# coins = []
# for i in range(n):
#     coins.append(randint(0, 1))
# print(coins)

# emblem = 0
# tails = 0

# for i in range(len(coins)):
#     if coins[i] == 0:
#         emblem += 1
#     else:
#         tails += 1

# if emblem < tails:
#     print(emblem)
# else:
#     print(tails)



# print('enter sum of numbers: ')
# s = int(input())

# print('enter product of numbers: ')
# p = int(input())

# for x in range(1, 1000):
#     for y in range(1, 1000):
#         if x + y == s and x * y == p and x <= y:
#             print(x, y)
        


# print('enter n: ')
# n = int(input())

# res = 1
# while res <= n:
#     print(res)
#     res = res * 2



# from random import randint 

# print('enter n: ')
# n = int(input())
# numbers_list = []

# for i in range(n):
#     numbers_list.append(randint(-3, 3))
# print(numbers_list)

# numbers_list.sort()
# print(numbers_list)

# count = 0
# for i in range(len(numbers_list)):
#     if numbers_list[i] != numbers_list[i-1]:
#         count += 1
# print(count)



# n = int(input('enter size of list: '))
# numbers_list = list(range(1, n+1))
# print(numbers_list)

# numbers_list1 = []
# k = int(input('enter k: '))
# for i in range(n):
#     if i >= k:
#         numbers_list1.append(numbers_list[i])

# for i in range(n):
#     if i < k:
#         numbers_list1.append(numbers_list[i])
# print(numbers_list1)



# v = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}] 

# v2 = []
# for i in v:
#     for k, v in i.items():
#         if v.strip() not in v2:
#             v2.append(v.strip())

# print(v2)



# from random import randint

# list = []
# n = int(input('enter n: '))
# for i in range(n):
#     list.append(randint(-5, 5))
# print(list)

# count = 0
# for i in range(1, len(list)):
#     if list[i] > list[i-1]:
#         count += 1

# print(count)


# from random import randint

# list = []
# n = int(input('enter number of size list: '))

# for i in range(n):
#     list.append(randint(1, n))
# print(list)

# k = int(input('enter number: '))
# count = 0
# for i in range(len(list)):
#     if list[i] == k:
#         count += 1
# print(f'-> {count}')


# from random import randint

# list = []
# n = int(input('enter number of size array: '))
# for i in range(n):
#     list.append(randint(1, 11000))
# print(list)

# x = int(input('enter number: '))
# m = [abs(list[i] -x) for i in range(len(list))]

# print(list[m.index(min(m))])


# dict_scrabble = {1:'AEIOULNSTRАВЕИНОРСТ', 2:'DGДКЛМПУ', 3:'BCMPБГЁЬЯ', 4:'FHVWYЙЫ', 5:'KЖЗХЦЧ', 8:'JXШЭЮ', 10:'QZФЩЪ'}

# k = input('enter any word: ')
# res = 0
# for i in k:
#     for key in dict_scrabble:
#         if i.upper() in dict_scrabble[key]:
#             res += key
# print(res)


# string = input('enter any string: ')

# s = 'a a a b c a a d c d d'
# s = s.split()

# dt = {}
# for i in s:
#     if i not in dt:
#         dt[i] = 0 # = 1
#         print(i, end=' ')
#     else:
#         dt[i] += 1
#         print(f'{i}_{dt[i]}', end=' ')  # print(f'{i}_{dt[i]-1}', end=' ')


# text = "She sells sea shells on the sea shore The shells\
#  that she sells are sea shells I'm sure. So if she sells sea\
#  shells on the sea shore I'm sure that the shells are sea\
#  shore shells"

# words = text.lower().replace('.', ' ').split()
# print(words)
# st = set(words)
# print(len(st))


# var2 = '10 20 30 40 50'
# var3 = '10 20 30 40 50'

# res = sorted(list((set(var2.split()) & set(var3.split()))))
# print(*res)


# arr = [5, 8, 6, 4, 9, 2, 7, 3]

# arr_1 = []
# sum = 0
# for i in range(len(arr)):
#     sum = arr[i-2]+arr[i-1]+arr[i]
#     arr_1.append(sum)
    
# print(max(arr_1))


# def fib(n):
#     if n <= 2:
#         return 1
#     return fib(n-1) + fib(n-2)

# k = int(input('enter number of fib: '))
# print(fib(k+1))


# a = [1, 5, 2, 4, 4]

# max_1 = max(a)
# min_1 = min(a)

# for i in a:
#     if a[i] == max_1:
#         a[i] = min_1
# print(a)


# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True


# k = int(input('Enter num: '))
# print('Yes' if is_prime(k) else 'No')


# import math

# def is_prime(n):
#     for i in range (2, math.ceil(math.sqrt(n))):
#         if n % i == 0:
#             return False
#     return True


# k = int(input('Enter num: '))
# print('Yes' if is_prime(k) else 'No')



# def reverse(n):
#     s = input()
#     if n == 1:
#         return s
#     return reverse(n-1) + ' ' + s


# n = int(input())    
# print(reverse(n))



# def exp(n, m):
#     if m == 0:
#         return 1
#     return n * exp(n, m-1) 


# a = int(input())
# b = int(input())
# print(exp(a, b))



# def sum(a, b):
#     if b == 0:
#         return a + b
#     return sum(a+1, b-1)

# a = int(input())
# b = int(input())
# print(sum(a, b))



# n = int(input('enter N: '))
# list_1 = []
# for i in range(n):
#     list_1.append(int(input()))
# print(list_1)
# m = int(input('enter M: '))
# list_2 = []
# for i in range(m):
#     list_2.append(int(input()))
# print(list_2)

# for i in list_1:
#         if i not in list_2:
#             print(i, end=' ')



# n = int(input('enter N: '))
# list_1 = []
# for i in range(n):
#     list_1.append(int(input()))
# print(list_1)

# count = 0
# for i in range(1, len(list_1)-1):
#     if list_1[i] > list_1[i-1] and list_1[i] > list_1[i+1] and list_1[i-1] == list_1[i+1]:
#         count += 1
# print(count)



# n = int(input('enter N: '))
# list_1 = []
# for i in range(n):
#     list_1.append(int(input()))
# print(list_1)

# count = 0
# for i in range(len(list_1)-1):
#     for j in range(i+1, len(list_1)):
#         if list_1[i] == list_1[j]:
#             count += 1
# print(count)


# from collections import Counter

# list_1 = [1, 2, 3, 2, 3, 3, 3]
# count = 0

# cnt = dict(Counter(list_1))
# print(cnt)

# for n in cnt.values():
#     count += n * (n-1) // 2
# print(count)
    


# def sum_del(n):
#     res = [1]
#     for i in range(2, n//2+1):
#         if n % i == 0:
#             res.append(i)
#     return sum(res)

# k = int(input())
# st = set()
# for number in range(k+1):
#     kandidat = sum_del(number)
#     if sum_del(kandidat) == number and kandidat != number:
#         st.add(tuple(sorted((number, kandidat))))

# for a, b in st:
#     print(a, b)



# a, b, c = map(int, input().split())

# lst = []
# for i in range(c):
#     lst.append(a)
#     a+=b
# print(*lst)



# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

# min_number = 0
# max_number = 10

# res = []
# for i in range(len(list_1)):
#     if list_1[i] >= min_number and list_1[i] <= max_number:
#         res.append(i)
# print(*res, sep='\n')



# lst = [1, 2, 3, 5, 8, 15, 23, 38]

# lst1 = []
# for i in lst:
#     if i % 2 == 0:
#         lst1.append((i, i**2))
# print(lst1)



# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# lst = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, lst)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)



# transformation = lambda i: i
# # values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# values = [1, 23, 42, 'asdfg']
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')



# def find_farthest_orbit (orbits):
#     filtered_orbits = list(filter(lambda orbit: orbit[0] != orbit[1], orbits))
#     squares = list(map(lambda orbit: orbit[0] * orbit[1], filtered_orbits))
#     maximum = max(squares)
#     res = list(filter(lambda orbit: orbit[0]*orbit[1] == maximum, filtered_orbits))
#     return res[0]


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# find_farthest_orbit (orbits)

# print(*find_farthest_orbit(orbits))



# def find_farthest_orbit (orbits):
#     # filtered_orbits = list(filter(lambda orbit: orbit[0] != orbit[1], orbits))
#     # return max(filtered_orbits, key=lambda orbit: orbit[0] * orbit[1])

#     return max(filter(lambda orbit: orbit[0] != orbit[1], orbits), key=lambda orbit: orbit[0] * orbit[1])


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# find_farthest_orbit (orbits)

# print(*find_farthest_orbit(orbits))



# def same_by(characteristic, objects):
#     lst = []
#     for obj in objects:
#         lst.append(characteristic(obj))

#     lst_map = list(map(characteristic, objects))
#     print(lst)
#     print(lst_map)

#     n = len(set(lst))
#     return n ==1 or n == 0
#     # return len(set(lst)) in (0, 1)  


# values = [0, 2, 10, 6] 
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')



# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# vowels = 'уеаыоэяию'
# phrases = stroka.split()

# vowels_list = []

# print(phrases)
# for ph in phrases:
#     count = 0
#     for j in ph:
#         if j in vowels:
#             count += 1
#     vowels_list.append(count)
# print(vowels_list)

# if len(vowels_list) == 1:
#     answer = 'Количество фраз должно быть больше одной!'
# elif len(set(vowels_list)) == 1:
#     answer = 'Парам пам-пам'
# else:
#     answer = 'Пам парам'

# print(answer)



# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows < 2 or num_columns < 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!') 
#     else:
#         header = ' '.join([str(i) for i in range(1, num_columns + 1)])   
#         print(header)
#         for i in range(2, num_rows + 1):
#             row = [str(i)] + [str(operation(i, j)) for j in range(2, num_columns + 1)]
#             print(' '.join(row)) 


# print_operation_table(lambda x, y: x * y)
# # print_operation_table(lambda x, y: x * y, 3, 3)



# file = open('text.txt')
# print(file.readlines())

# output = ['Hello', 'Python', '!']
# with open('text2.txt', 'w') as file:
#     # file.writelines(output)
#     file.write('\n'.join(output))