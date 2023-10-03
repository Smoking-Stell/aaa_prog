def hierarchy_write(departments: dict):
    """
    Visualize the structure of teams and departments

    :param departments: dict of sets with teams
    :return: nothing
    """

    for depart in departments.keys():
        print(f"Департамент: {depart}\n Команды:")
        for team in departments[depart]:
            print(f"    {team}")


def hierarchy(table: list):
    """
    Makes a structure of departments and teams. After that write all of them in console

    :param table: list of list which contains all information from csv
    :return: nothing
    """
    depart_hierarchy = {}
    for row in table:
        depart = row[1]
        team = row[2]

        if depart not in depart_hierarchy:
            depart_hierarchy[depart] = set()
        depart_hierarchy[depart].add(team)

    hierarchy_write(depart_hierarchy)


def departments_review(table: list):
    print(3)


def csv_save(table: list):
    print(2)


def read_file_csv(file_name: str) -> list:
    data = []
    with open(file_name, 'r', encoding = 'utf-8') as file:
        next(file)
        for line in file:
            stripped_line = line.strip()
            column = stripped_line.split(';')
            data.append(column)
    return data


def menu():
    menu_options = {1: hierarchy,
                    2: departments_review,
                    3: csv_save}

    option = 0
    while option not in menu_options.keys():
        print("Write '1' if you want to see hierarchy of departments\n"
              "'2' if you want to see departments review\n"
              "'3' if you want to save review in new csv")
        option = input()
        option = int(option)
    print("Write file name without .csv")
    file_name = input()
    file_name = "{}{}".format(file_name, ".csv")
    table = read_file_csv(file_name)
    menu_options[option](table)


if __name__ == '__main__':
    menu()
