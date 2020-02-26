validate_str = """\/:*?<>"|"""


def check_validate_name_folder(name):
    for char in name:
        if char in validate_str:
            name = name.replace(char,'')
    return name.replace(" ", "_").lower()
print(check_validate_name_folder("An: Entire| MBA ?in 1 *Course:Award <Winning> Business? School Prof"))