def print_formatted(number):
    b = bin(number)[2:]
    master_width = len(b)
    for i in range(1, number+1):
        d = str(i)
        o = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bi = bin(i)[2:]
        print(d.rjust(master_width), o.rjust(master_width), hexa.rjust(master_width), b.rjust(master_width))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)