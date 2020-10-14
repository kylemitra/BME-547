def my_funct():
    # Exception Error
    myList = [1,2,3]
    try:
        for i in range (0,4):
            if i >len(myList):
                # Another way to do this
                # raise IndexError('ERROR: Make sure your index values are within range!')
            print(myList[i])
    except IndexError:
        print('ERROR: Make sure your index values are within range!')
    except: # This is typically bad practice
        print('You have a non-IndexError error')
    # else: # Another way to do this
    #     print('You have a non-IndexError error')

    # Syntax Error
    # for i in range(0,5)
    #     print(i)

def main():
    my_funct()

if __name__ == '__main__':
    main()