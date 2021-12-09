import random

initial_state = "123456789"
cell_list = []
coordinate_list = []
check_list = [1, 2, 3]
for x in initial_state:
    cell_list.append(" ")
cell_map = {1: [cell_list[0], cell_list[1], cell_list[2]],
            2: [cell_list[3], cell_list[4], cell_list[5]],
            3: [cell_list[6], cell_list[7], cell_list[8]]
            }


def grid_output(map):
    print("---------")
    print(f"| {map.get(1)[0]} {map.get(1)[1]} {map.get(1)[2]} |")
    print(f"| {map.get(2)[0]} {map.get(2)[1]} {map.get(2)[2]} |")
    print(f"| {map.get(3)[0]} {map.get(3)[1]} {map.get(3)[2]} |")
    print("---------")


def cd_input(coordinate_list):
    coordinate_list.clear()
    coordinates = input("Enter the coordinates: ")
    for cd in coordinates.split():
        coordinate_list.append(cd)
    return coordinate_list


def is_valid_number(cd_list):
    for number in cd_list:
        if len(number) > 1:
            print("You should enter numbers!")
            cd_input(cd_list)
        else:
            if int(number) not in check_list:
                print("Coordinates should be from 1 to 3!")
                cd_input(cd_list)


grid_output(cell_map)
cd_input(coordinate_list)


def easy_ai_move(map):
    ai_coordinates = [random.randint(1, 3), random.randint(1, 3)]
    if map.get(ai_coordinates[0])[ai_coordinates[1] - 1] == "X" or map.get(ai_coordinates[0])[ai_coordinates[1] - 1] == "O":
        print("This cell is occupied! Choose another one!")
        easy_ai_move(map)
    else:
        map.get(ai_coordinates[0])[ai_coordinates[1] - 1] = "O"
        print('Making move level "easy"')
        grid_output(map)


def human_move(coordinate_list, map):
    is_valid_number(coordinate_list)
    if map.get(int(coordinate_list[0]))[int(coordinate_list[1]) - 1] == "X" or map.get(int(coordinate_list[0]))[int(coordinate_list[1]) - 1] == "O":
        print("This cell is occupied! Choose another one!" + "human")
        cd_input(coordinate_list)
        human_move(coordinate_list, map)
    else:
        map.get(int(coordinate_list[0]))[int(coordinate_list[1]) - 1] = "X"
        grid_output(map)


def whos_next(coordinate_list, map):
    x_counter = 0
    o_counter = 0
    for x in map.keys():
        for index in range(0, 3):
            if map.get(x)[index] == "X":
                x_counter += 1
            elif map.get(x)[index] == "O":
                o_counter += 1
    if x_counter == o_counter:
        human_move(coordinate_list, map)
    elif x_counter > o_counter:
        easy_ai_move(map)


def win_checker(cd_list, map):
    print("win checker")
    print(map.get(1)[0] + " " + map.get(2)[1] + " " + map.get(3)[2])
    if map.get(1)[0] == map.get(2)[1] == map.get(3)[2] and map.get(1)[0] != " ":
        print(map.get(2)[1] + " wins")
        return
    if map.get(1)[2] == map.get(2)[1] == map.get(3)[0] and map.get(3)[0] != " ":
        print(map.get(2)[1] + " wins")
        return
    for x in map.keys():
        if map.get(x)[0] == map.get(x)[1] == map.get(x)[2] and map.get(x)[0] != " ":
            print(map.get(x)[0] + " wins")
            return
    for x in map.keys():
        if map.get(1)[x-1] == map.get(2)[x-1] == map.get(3)[x-1] and map.get(1)[x-1] != " ":
            print(map.get(1)[x-1] + " wins")
            return
    for x in map.keys():
        if map.get(x)[0] == " " or map.get(x)[1] == " " or map.get(x)[2] == " ":
            whos_next(cd_list, map)
            win_checker(cd_list, map)
        else:
            print("Draw")


win_checker(coordinate_list, cell_map)
grid_output(cell_map)
