def rem(l,word):
    n=[]
    for items in l:
        if not(items==word):
            n.append(items.strip(word))
        
    return n

l=["sanket","naerya","Bappu","kayrebho"]
print(rem(l,"a"))