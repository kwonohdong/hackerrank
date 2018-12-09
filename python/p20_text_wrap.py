import textwrap

def wrap(string, max_width):
    # ABCDEFGHIJKLIMNOQRSTUVWXYZ (24)
    # ABCD, EFGH, IJKL, IMNO, QRSTU, VWXYZ
    
    # solution 1
    # iter_cnt = len(string) / max_width + 1 if len(string) % max_width == 1 else len(string) / max_width
    # result = []
    # for i in range(iter_cnt):
    #     result.append(string[i*max_width:max_width*(i+1)])
    # return "\n".join(result)

    # solution 2
    # return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])
    return "\n".join(textwrap.wrap(string, max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)