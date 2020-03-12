#
#Chapter 7 Project part 1 High and low.
#Input- The user enters a number that is stored and displays the lowest and highest number
#Processing- The program stores the numbers entered into a list and prints the lowest and highest number
#Output- The prgram prints the lowest and highest number entered in the list.



def main():
    list = []
    print('Please enter a number, if number = -99, the program will stop')
    item = int(input())
    while item != -99:
        list.append(item)
        item = int(input())
    SelectionSort(list)
    print(list[0], list[-1])

def SelectionSort(list):
    firstUnsorted = 0
    while firstUnsorted < len(list)-1:
        indexSmall = findSmallest(list, firstUnsorted)
        swap(list, indexSmall, firstUnsorted)
        firstUnsorted = firstUnsorted + 1
        
def findSmallest(list, first):
    small = first
    index = first + 1
    while index <= len(list)-1:
        if list[index] < list[small]:
            small = index
        index = index + 1
    return small

def swap(list, index1, index2):
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp

main()
