def main():
    """this funtion will test if two number are divisable or not and print a responce """
    frist_num = vaild_number()
    second_num = vaild_number()
    new_numb = int(frist_num) / int(second_num)
    if new_numb > 1:
        print("yes the number is divisable")
    else:
        print("no the number isn't divisable")

def vaild_number():
    number = input("whats the number: ")
    while int(number) > 0:
        return number
    number = input("whats the number: ")

    


main()