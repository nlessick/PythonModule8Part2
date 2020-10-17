def in_dict(check_dict):
    return "Does the dictionary contain A? ", 'A' in check_dict

if __name__ == '__main__':
    my_dict = {'A':1,'B':2,'C':3,'D':4,'E':5}
    print("My set contains: ", my_dict)
    print(in_dict(my_dict))
