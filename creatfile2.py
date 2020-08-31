import os

def get_fname():
    while True:
        fn = input("请输入文件名: ")
        if not os.path.exists(fn):
            break
        print('文件已存在，请重新输入')
    return fn

def get_content():
    cont = []
    print("请输入内容，end结束：")
    while True:
        line = input("请输入: ")
        if line == 'end':
             break
        cont.append(line+"\n")
    return cont


def write_file(fname,content):
    with open(fname,'w') as f:
        f.writelines(content)



if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    write_file(fname,content)