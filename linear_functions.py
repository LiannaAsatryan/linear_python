#this function receives a string line as a parameter,
#splittes it into two parts, and returns that two parts
def get_nums(line):
    temp = line.split()
    return (str(temp[0]), str(temp[1]))


#this function returns true if the given string 
#is a real number
def is_float(str):
    try: 
        float(str)
    except ValueError: 
        return False
    return True

#this function solves the ax+b=0 linear equation, where str1=a, str2=b
#and returns the answer as a string
def linear(str1, str2):
    if (not is_float(str1)) or (not is_float(str2)):
        return 'mistake'
    else:
        a = float(str1)
        b = float(str2)
        if (a == 0 and b == 0):
            return "R"
        elif (b != 0 and a == 0):
            return "no solution"
        elif (b == 0):
            return "0"
        else:
            d = float("{0:.3f}".format(- b / a))
            if (d.is_integer()):
                d = int(d)
            return str(d)



