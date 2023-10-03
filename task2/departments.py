MAX_SALARY = 10**9


def hierarchy_visualize(departments: dict):
    """
    Visualize the structure of teams and departments

    :param departments: dict of sets with teams
    :return: nothing
    """

    for depart in departments.keys():
        print(f"Department: {depart}\n Teams:")
        for team in departments[depart]:
            print(f"    {team}")


def hierarchy(table: list):
    """
    Makes a structure of departments and teams. After that write all of them in console

    :param table: list of lists which contains all information from csv
    :return: nothing
    """

    depart_hierarchy = {}
    for row in table:
        depart = row[1]
        team = row[2]

        if depart not in depart_hierarchy:
            depart_hierarchy[depart] = set()
        depart_hierarchy[depart].add(team)

    hierarchy_visualize(depart_hierarchy)


def update_dep_info(curr_info: list, salary: int) -> list:
    """
    recounts information for department when we add new employee

    :param curr_info: current list:
    [number of employees, min salary, max salary, average salary]
    :param salary: salary of new employee
    :return: updated info
    """

    curr_info[1] = min(curr_info[1], salary)
    curr_info[2] = max(curr_info[2], salary)
    curr_info[3] *= curr_info[0]
    curr_info[0] += 1
    curr_info[3] = (curr_info[3] + salary) / curr_info[0]

    return curr_info


def info_visualize(departments_info: dict):
    """
    Visualize information about each department:
    Name, number of employees, min and max salary, average salary

    :param departments_info: short info review of each department:
        Name, number of employees, min and max salary, average salary
    :return: nothing
    """

    print(f"Department, number of employees, Min-Max salary, average salary")

    for dep in departments_info:

        curr_dep = departments_info[dep]
        print(f"{dep}, {curr_dep[0]}, {curr_dep[1]} - {curr_dep[2]},"
              f" {round(curr_dep[3])}\n")


def departments_info_build(table: list) -> dict:
    """
    Makes a short info review of each department:
    Name, number of employees, min and max salary, average salary

    :param table: list of lists which contains all information from csv
    :return: dict
    """

    departments_info = {}
    for row in table:
        depart = row[1]
        salary = int(row[5])
        if depart not in departments_info.keys():
            departments_info[depart] = [1, salary, salary, salary]
        else:
            departments_info[depart] = update_dep_info(departments_info[depart], salary)

    return departments_info


def departments_review(table: list):
    """
    Makes a short info about department and then visualize it

    :param table: list of lists which contains all information from csv
    :return: nothing
    """

    info_visualize(departments_info_build(table))


def dict_to_csv(department_info: dict):
    """
    Convert dict of department information to csv file

    :param department_info: short info review of each department:
        Name, number of employees, min and max salary, average salary
    :return:
    """

    headers = ["Department", "number of employees", "Min-Max salary", "average salary"]

    with open('dept_info.csv', 'w', encoding='utf-8') as f:
        f.write(';'.join(headers) + '\n')

        for key, values in department_info.items():
            row = [key] + values
            f.write(';'.join(map(str, row)) + '\n')


def csv_save(table: list):
    """
    Get information from csv and then reorganise it to short info for each department

    :param table: list of lists which contains all information from csv
    :return: nothing
    """

    department_info = departments_info_build(table)
    dict_to_csv(department_info)


def read_file_csv(file_name: str = "Corp_Summary") -> list:
    """
    Read csv file, parse it and convert to list of lists, where each list is row

    :param file_name: name of input file without csv
    :return: list of lists which contains information from csv
    """

    file_name = "{}{}".format(file_name, ".csv")
    data = []
    with open(file_name, 'r', encoding='utf-8') as file:
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

    table = read_file_csv(file_name)
    menu_options[option](table)


if __name__ == '__main__':
    menu()
