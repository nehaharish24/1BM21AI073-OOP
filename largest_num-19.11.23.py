def largest(list1):
  max=list1[0]
  for num in list1:
      if num > max:
          max=num
          
  return max

print("program to find the largest element in a list")
print("enter the number of elements in the list")
n=int(input())
list1=[]
print("enter the numbers")
for i in range(n):
    num=int(input())
    list1.append(num)
    

largest_num=largest(list1)
print("the largest number is ",largest_num)
