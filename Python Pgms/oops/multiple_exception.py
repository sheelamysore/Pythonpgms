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
        
except (TypeError, ZeroDivisionError) as e:
    print(e)   
         
except Exception as e:
    print(e)
    