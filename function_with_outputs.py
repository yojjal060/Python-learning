def format_name():
    f_name = input("Enter your first name: ")
    l_name = input("Enter your last name: ")
    title1 = f_name.title()
    title2 = l_name.title()
    output = print(f"{title1} {title2}")
    return output

format_name()

lens = len("Yojjal")
print(lens)