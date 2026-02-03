def swap_case(s):
    res = []
    for char in s:
        if "A" <= char <= "Z":
            res.append(chr(ord(char) + 32))
        elif "a" <= char <= "z":
            res.append(chr(ord(char) - 32))
        else:
            res.append(char)
    return "".join(res)

if __name__ == '__main__':
    s = input()
    print(swap_case(s))