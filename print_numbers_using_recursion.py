def natural_numbers(max_number):
    if max_number >= 1:
        print(max_number, end=" ")
        natural_numbers(max_number - 1)

exec("natural_numbers(100)")
eval("natural_numbers(100)")
