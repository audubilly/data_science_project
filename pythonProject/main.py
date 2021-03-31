# # name = input('what is your name: ')
# # print('my name  is name: ' + name)
#
# #
# # print(type(6))
# # print(type('billy'))
# #
# # print(type(5 // 4))
# #
# # print(bin(7))
# # print(int('0b111', 2))
# #
#
# int
# float
# complex
# str
# list
# tuple
# bool
# set
# dict
#
# # long_str = '''
# # WOW
# # O O
# # ---
# # '''
#
# # print(long_str)
# # print(long_str)
# #
# # name = input('please Enter your name: ')
# # age =input('Enter your age:  ')
# #
# # print(f'My name is {name},i am {age} years old, \nHope you are doing great today')
# # print(type(age))
#
# # base = float(input('enter base: '))
# #
# #
# # height = float(input('Enter height:'))
# #
# # area = 0.5 * (base * height)
# # print(f'area is {area}')
# # print('we put base {} and height {} in the formulae to give area {}'.format(base,height,area))
#
#
# selfish = '01234567'
# # 01234567
# # (start:stop:stepover)
# # print(selfish[:-1])
#
# # name = 'helllloooooooo'
# # print(name.isprintable())
# # print(name.isdecimal(), name.isprintable(), name.islower(), name.isidentifier(), name.upper(), name.capitalize(), name.casefold(), )
# # # print(len(name))
# # # print(type(14))
# #
# # print(bool('true'))
#
# # birth_year = input('what year where you born: ')
# # age = 2021 - int(birth_year)
# # print(f'You are {age} years old')
#
#
# amazon_cart = ['sunglasses', 'shoes', 'notebooks', 'clothes', 'bicycle', 'houses', 'video_games']
# amazon_cart[3] = 'hoodies'
# amazon_cart[2] = 'jackets'
#
# # ADDING ITEMS
# amazon_cart.append('grapes')
#
# amazon_cart.insert(3, 'boxers')
#
# amazon_cart.extend(['jump', 'juice', 'jameson'])
#
# print(amazon_cart)
#
# # new_cart = amazon_cart[:]
# #
# # new_cart= amazon_cart[2:]
# #
# # print(new_cart)
# # print(amazon_cart)
#
# # print(amazon_cart[0:2])
# #
# # new_cart = amazon_cart
# # new_cart = amazon_cart[:]
# # new_cart[0] = 'kettle'
# # print(new_cart)
# # print(amazon_cart)
#
#
# # REMOVING ITEMS
# amazon_cart.pop(3)
# print(amazon_cart)
#
# amazon_cart.pop(5)  # to pop off an item off a list via the INDEX.
# print(amazon_cart)
#
# amazon_cart.remove('jackets')  # to remove an item from a list .
# print(amazon_cart)
#
# # amazon_cart.clear() # to clear a list totally.
# # print(amazon_cart)
#
# print('shoes' in amazon_cart)  # (in() fuction to check if a value is in a list)
#
# # amazon_cart.sort()
# # print(amazon_cart) #ARRANGES THE LIST PROPERLY FOR YOU
#
# print(sorted(amazon_cart))  # THIS IS AMETHOD AND ANOT A FUNCTION
#
# print(len(amazon_cart))
#
# new_sentence = ' '.join(['hey', 'my', 'name', 'is'])  # TO JOIN STRINGS
# print(new_sentence)
#
# dictionary = {'a': [1, 2, 3, 4],
#               'b': ['boy', 'girl'],
#               'c': True,
#               'd': 54
#
#               }
# for item in dictionary:
#     print(item)
#
# # {'c': False,
# #  'd': [4, 5, 6, 7],
# #  'e': 'hello'}]
#
# # print(dictionary[0]['a'][2])
# print(dictionary.get('a')[2])
#
# print(dictionary.update({'d': 65}))
# print(dictionary)
#
# # print(dictionary.clear())
# # print(dictionary)
#
# print(dictionary.values())
#
# print(dictionary.items())
#
# my_tuple = [1, 2, 3, 4, 5, 6]
# print(my_tuple[2])  # Getting values in a tuple.
#
# print(5 in my_tuple)
#
# print(my_tuple.copy())
# # print(my_tuple.clear())
#
# my_set = {1, 2, 3, 4, 5, 5, 5, 4}
# # print(set(my_list))
#
# your_set = {34, 3, 4, 76, 6, 7, 13, 8, 9}
#
# print(my_set.difference(your_set))  # Set methods.
#
# (my_set.discard(5))
# print(my_set)
#
# print(my_set.difference_update(your_set))
# # print(my_set)
#
# my_set.intersection(your_set)
# print(my_set)
# print(my_set & your_set)
#
# # print(my_set)
#
# print(my_set.union(your_set))
# print(my_set | your_set)  # short hand for union.
#
# print(my_set.isdisjoint(your_set))
#
# print(my_set.issubset(your_set))
#
# print(my_set.issuperset(your_set))
#
# # my_set.add(18)
# # my_set.add(100)
# # my_set.add(2)
# # print(my_set)
# #
# # print(len(my_set))
#
# is_old = False
#
# if is_old:
#     print('you can drive the car')
# else:
#     print('you are under aged')  # If conditional statement
#
# is_friend = True
#
# can_message = 'Message allowed' if is_friend else 'Message not allowed'  # Ternary operator
# print(can_message)
#
# for item in 'my new world ':
#     print(item)

# scores = {64, 34, 56, 76, 88}
#
# print(scores)
#
# scores.append(45)
# print(scores)
#
# scores.insert(0, 99)
# print(scores)
#
# scores[0] += 1
# print(scores)
#
# scores += [12]
# print(scores)
#
# scores.remove(scores[3])
# print(scores)
#
# scores.pop()
# print(scores)
#
# names = ["jude", "junior", "jack"]
# names_joined = " * ".join(names)
# print(names_joined)
#
# # scores = (64, 34, 56, 76, 88)

first_int = 10
second_int = 20

if first_int > second_int:
    print("the first int is larger!")

else:
    print("the second int is bigger!")


