#3th greeting
def greet(name, owner):
    if name == owner:
        return("Hello boss")
    return("Hello guest")



#4th i failed

#my solution:
def repeat_str(repeat, string):
    str2 = string
    while repeat > 1:
        string = string + str2 
        repeat = repeat -1
    return(string)
#other's solution:
def repeat_str(repeat, string):
    return repeat * string
#or 
def repeat_str(repeat, string):
    solution = ""
    for i in range(repeat):
        solution += string
    return solution


#5th
#
def solution(number):
    sums = 0
    for i in range(number):
        if i%3 == 0 or i%5 == 0:
            sums += i
        elif i <= 0:
            return(0) 
    return (sums)
  
#other's solutions
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
  


print(solution(6))

#finished at 12:52PM 12/21/2022 