def demo():
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
    # Press the green button in the gutter to run the script.
    if __name__ == '__main__':
        demo()