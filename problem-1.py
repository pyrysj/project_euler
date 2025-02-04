# do it in a really boring way
list = [n for n in range(1,10) if n % 5 == 0 or n % 3 == 0]
# then we can just sum the list
res_base = sum(list)
print(res_base)

# this can now be easily expanded 
list_problem = [n for n in range(1,1000) if n % 5 == 0 or n % 3 == 0]
answer = sum(list_problem)
print(answer)