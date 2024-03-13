# test = "hello hi"
test = "this is simple reverse string approach example"


def reverse_string(string):
    # base case
    if string == "":
        return ""
    return reverse_string(string[1:]) + string[0]


print(reverse_string(test))
