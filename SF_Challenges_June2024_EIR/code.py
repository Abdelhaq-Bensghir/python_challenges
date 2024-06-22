if __name__ == '__main__':
    import re
    with open('input/file1.txt','r') as file:
        c=file.readlines()
        lines = [i.strip('\n') for i in c]
        # reg = re.compile(r'(\w+)\((\d+?\.*\d*)\)\s*([\+\-\*\/])\s*(\w+)\((\d+?\.*\d*)\)')
        reg = re.compile(r'(\w+)\((\d+?\.*\d*)\)\s*([\+\-\*\/])\s*(\w+)\((\d+?\.*\d*)\)')
        for line in lines:
            output = reg.search(line)
            elements = output.groups()