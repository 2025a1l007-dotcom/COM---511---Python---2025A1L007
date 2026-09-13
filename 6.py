user_input = input("Enter a value: ")

# Without typecasting (repeats the string 3 times)
str_result = user_input * 3

# With typecasting to int (multiplies numerically)
int_result = int(user_input) * 3

print("Without typecasting (String multiplication):", str_result)
print("With typecasting to int (Integer multiplication):", int_result)