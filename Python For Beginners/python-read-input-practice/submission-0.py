def add_two_numbers() -> int:
    nums_s = input()
    nums_l = [int(x) for x in nums_s.split(",")]
    return sum(nums_l)


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
