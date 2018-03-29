def is_multiple(n,m):
    if (n%m == 0):
        return True
    else:
        return False

if __name__ == "main":
    a,b = input("Enter 2 integers:").split()
    print(is_multiple(int(a),int(b)))
