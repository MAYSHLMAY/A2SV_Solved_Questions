def split_and_join(line):
    result = ''
    for char in line:
        if char == ' ':
            result += '-'  
        else:
            result += char
    return result

if __name__ == '__main__':
    line = input()
    print(split_and_join(line))
