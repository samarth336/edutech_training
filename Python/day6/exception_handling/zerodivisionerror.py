def divide(a,b):
    try:
        result=a/b
    except ZeroDivisionError:
        return "Can't Enter Zero as Denominator"
    except TypeError:
        return "Enter numbers only"
    else:
        return result
    
print(divide(2,1))
print(divide(2,0))
print(divide("sd",0))