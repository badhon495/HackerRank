import textwrap

def wrap(string, max_width):
    list1 = textwrap.wrap(string, max_width)
    for i in list1:
        if [i] == list1[len(list1)-1:]:
            return i
        else:
            print(i)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
