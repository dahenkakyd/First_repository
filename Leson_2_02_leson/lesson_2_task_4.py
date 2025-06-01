n = int(input("Введите число:"))
def nums_3_5(n):
    for nums in range(1,n+1):
        if nums%3==0 and nums%5==0:
            print("Fizz_Buzz")
        elif nums%3==0:
            print("Fizz")
        elif nums%5==0:
            print("Buzz")
        else:
            print(nums)

nums_3_5(n)
