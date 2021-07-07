
def make_lower_fun1(string):
    return str(string).lower()


def make_lower_fun2(string):
    arr_of_chars = list(string)
    for i in range(0, len(arr_of_chars)):
        if 'A' <= arr_of_chars[i] <= 'Z':
            arr_of_chars[i] = chr(ord(arr_of_chars[i])+32)
    return "".join(arr_of_chars)


def main():
    string = "WasEEm SayRaZA"
    print(make_lower_fun1(string))
    print(make_lower_fun2(string))


main()
