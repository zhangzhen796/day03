import sys
import string
import keyword
first_str = string.ascii_letters + '_'
str = first_str + string.digits

def check_string(inp):
    if keyword.iskeyword(inp):
        return "%s is guanjianzi" % inp
    if inp[0] not in first_str:
        return "1 no"
    for i in range(len(inp)):
        if i == 0:
            continue
        if inp[i] not in str:
            return "di %s ge bu xing   %s" %(i+1,inp[i])
    return "all he ge"

if __name__ == '__main__':
    print(check_string(sys.argv[1]))