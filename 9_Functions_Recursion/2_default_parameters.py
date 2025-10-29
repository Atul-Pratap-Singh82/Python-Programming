def price(a,b=266.5): # defoult parameters are define in function definition ex(b=266.5). and defoult parameter defines from last.
    total=a*b
    print(total)
    return total

n=int(input("Enter a quantity: "))
price(n)