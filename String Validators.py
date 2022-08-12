if __name__ == '__main__':

    def alnum(s):
        for i in s:

            if i.isalnum():
                return True
        return False

    def alpha(s):
        for i in s:

            if i.isalpha():
                return True
        return False


    def digit(s):
        for i in s:

            if i.isdigit():
                return True
        return False

    def lower(s):
        for i in s:

            if i.islower():
                return True
        return False

    def upper(s):
        for i in s:

            if i.isupper():
                return True
        return False


s = input()
print(alnum(s))
print(alpha(s))
print(digit(s))
print(lower(s))
print(upper(s))
