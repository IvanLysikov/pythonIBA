# 8.Натуральное число, записанное в десятичной системе счисления, называется сверхпростым, если оно остается простым при
# любой перестановке своих цифр. Определить все сверхпростые числа до n.

# method checks if the number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# method gives all variants of digits in number, if all of them is prime
def all_variants(number):
    digits = [int(d) for d in str(number)]
    variants = set()
    end = len(digits)

    # recursion
    def generate_variants(index, current):
        if index == end:
            # the way to build number from array of digits:
            # num = int("".join(map(str, current)))
            num = ""
            for digit in current:
                num += (str(digit))
            num = int(num)
            if not is_prime(num):
                # it's my vision of turbo exit from recursion:
                raise Exception()
            variants.add(num)
        else:
            for i in range(index, end):
                current[index], current[i] = current[i], current[index]
                generate_variants(index + 1, current)
                current[index], current[i] = current[i], current[index]

    # this try block isn't necessary but helps to skip useless recursion calls
    try:
        generate_variants(0, digits)
    except Exception as e:
        return None
    return variants


print("You can use any number, but I believe that there is no such numbers after 991")
print("Besides for 1000000 it takes about 10 seconds to check all numbers!!!")
print("With big numbers comes BIG RESPONSIBILITY!!!")
user_input = int(input("Enter number:\n"))
out = set()
for i in range(user_input):
    if is_prime(i):
        if all_variants(i) is not None:
            out.add(i)

print(f"Super prime numbers from 0 to {user_input} is: {sorted(out)}")
