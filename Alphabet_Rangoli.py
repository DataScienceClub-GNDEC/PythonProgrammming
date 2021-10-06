def print_rangoli(size):
    string = "abcdefghijklmnopqrstuvwxyz"
    l=[]
    for i in range(size):
        s = '-'.join(string[i:size])
        l.append((s[::-1]+s[1:]).center(4*size -3,'-'))
    
    print("\n".join(l[size-1:0:-1]+l[:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)