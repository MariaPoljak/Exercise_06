#power(a,b)

def power(a: int, b: int):
    if a <= 0 or b <= 0:
        return_value = -1
    else:
        return_value = a * power(a, b - 1)


#binary_search(numbers, num)

def binary_search(numbers, num):
    if len(numbers) == 0:
        return -1                                       #empty list returns -1
    index = len(numbers) // 2
    if numbers[index] == num:
        return num                                      #num is in the middle, return num
    if num < numbers[index]:
        return binary_search(numbers[0:index], num)     #if num is smaller than middle, search left side
    return binary_search(numbers[index+1:], num)        #if num is bigger than middle, search right side