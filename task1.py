def calculate_squares(nums: list[int]) -> list[int]:

    result = []
    for n in nums:
        result.append(n * n)
    return result

user_input1 = input("Enter first list of numbers (space-separated): ")
list1 = list(map(int, user_input1.split()))

user_input2 = input("Enter second list of numbers (space-separated): ")
list2 = list(map(int, user_input2.split()))

squared1 = calculate_squares(list1)
squared2 = calculate_squares(list2)

print("Squares of first list:", squared1)
print("Squares of second list:", squared2)
