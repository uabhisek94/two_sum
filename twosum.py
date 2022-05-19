list_count = int(input('Enter how many numbers you want to count: '))
target = int(input('Enter your target number: '))
list_counter = 0
lists = []

print(f'Please Enter {list_count} of numbers')
while list_counter < list_count:
    ele = int(input(f'{list_counter + 1}: '))
    lists.append(ele)
    list_counter += 1

"======================================================================================================================"
nums = lists
count = 0
count_2 = 1
element1 = 0
element2 = 0
test = False

while count < len(nums):
    while count_2 < len(nums):
        if target == nums[count] + nums[count_2]:
            test = True
            element1 = count
            element2 = count_2
            break
        else:
            test = False
            count_2 += 1
    if test:
        break
    count += 1
    count_2 = count + 1

return_value = [element1, element2]
print(f"Your numbers from list are: {nums[element1]}, {nums[element2]}")
print(return_value)