list=[]
list=input("Enter the list of numbers separated by comma and space: ").split(", ")
element=input("Enter the element to search: ")
found=False
list=[int(x) for x in list]
for i in range(len(list)):
    for j in range(i+1, len(list)):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]
print("Sorted list:", list)
while(found==False):
    mid=len(list)//2
    if list[mid]==int(element):
        found=True
        print("Element found at index:", mid)
    elif list[mid]>int(element):
        list=list[:mid]
    else:
        list=list[mid+1:]