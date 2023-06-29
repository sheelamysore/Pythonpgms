try: 
    try:
        a=2+1
        print(a)
        b=3*2
        print(b)
        # c=2+"abc"
        # print(c)
        d=2/0
        print(d)
        e=5-2
        print(e)
        
        
    except TypeError as te:
        print(te)
        d=2/0
        print(d)
        e=5-2
        print(e)

except ZeroDivisionError as ze:
    print(ze)
    e=5/0
    print(e)
    
finally:
    print("This is final block")   