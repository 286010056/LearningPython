
# https://mp.weixin.qq.com/s/7_1V6nAfZFHxgRClQ6hO2w

# 10个我花了很久才理解的Python概念——直到我看到这些例子！

def add(items, value):
    items.append(value)
    return items

my_list=[1,2,3]
print(id(my_list))
add(my_list,4)
print(my_list)

my_list = [1, 2, 3]
print(id(my_list))  # 输出变量的内存地址

# 对比两个变量是否指向同一内存地址
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print(id(list1))  # 相同的内存地址
print(id(list2))  # 相同的内存地址
print(id(list3))  # 不同的内存地址

print('hello,world')

my_tuple = (1, 2, 3)
#my_tuple.append(4)  # 会报错

def add_to_list(new_item, items=[]):
    items.append(new_item)
    return items

# Example usage:
print(add_to_list(1))  # Output: [1]
print(add_to_list(2))  # Output: [1, 2] - expected: [2]

def add_to_list2(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_to_list2(1))  # Output: [1]
print(add_to_list2(2))  # Output: [2]

# List comprehension: builds the full list in RAM
squares = [x**2 for x in range(5)]

# Generator expression: generates items on-the-fly, using less memory
squares_gen = (x**2 for x in range(5))

print("List comprehension result:", squares)
print("Generator expression result:", list(squares_gen))

print("End")