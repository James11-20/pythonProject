from useful_functions import *
import Character_Class
#or from Character_Class import character
def demo():

    print(do_addition(3,8))
    print(print_loud('HELLO'))
    # the ": str" is a python type hint
    my_name: str = "Jim"
    number: int = 167
    print(my_name, number)

    # printing functions using a format String
    print(f'Hello, My name is {my_name}')
    print(f'The answer is {5+8}')

    slice_str = my_name[1]
    print(slice_str)

    long_name = "Asshat"
    as_slice = long_name[0:4]
    print(as_slice)

    counter=0
    while counter <10:
        print(counter)
        counter+=1

    for index in range(10):
        print(index,end='\n')
    file_obj = open('text_file.txt')
    print(type(file_obj))
    print(file_obj)
    print(file_obj.readline())
    print(file_obj.read())
    file_obj.seek(10)

    file_obj.close()

    with open('text_file.txt','r') as file_obj2:
        file_obj2.readline()

    character = {
        'npc_type': 'car'
    }
    npc1 = Character_Class.Character()
    print(npc1)
#

    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    demo()