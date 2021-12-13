import random

initial_state = "123456789"
cell_list = []
coordinate_list = []
check_list = [1, 2, 3]
for x in initial_state:
    cell_list.append(" ")
start_list = ["start", "easy", "human"]

cell_map = {1: [cell_list[0], cell_list[1], cell_list[2]],
            2: [cell_list[3], cell_list[4], cell_list[5]],
            3: [cell_list[6], cell_list[7], cell_list[8]]
            }


def first_input():
    answer = []
    start = input()
    for word in start.split():
        if word == "exit":
            exit()
        else:
            answer.append(word)
    if len(answer) < 3:
        print("Bad parameters!")
        first_input()
    return answer


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


def easy_ai_move(map, move):

    ai_coordinates = [random.randint(1, 3), random.randint(1, 3)]
    if map.get(ai_coordinates[0])[ai_coordinates[1] - 1] == "X" or map.get(ai_coordinates[0])[ai_coordinates[1] - 1] == "O":
        print("This cell is occupied! Choose another one!")
        easy_ai_move(map, move)
    else:
        map.get(ai_coordinates[0])[ai_coordinates[1] - 1] = move
        print('Making move level "easy"')
        grid_output(map)


def human_move(coordinate_list, map, move):

    is_valid_number(coordinate_list)
    cd_input(coordinate_list)
    if map.get(int(coordinate_list[0]))[int(coordinate_list[1]) - 1] == "X" or map.get(int(coordinate_list[0]))[int(coordinate_list[1]) - 1] == "O":
        print("This cell is occupied! Choose another one!")
        cd_input(coordinate_list)
        human_move(coordinate_list, map)
    else:
        map.get(int(coordinate_list[0]))[int(coordinate_list[1]) - 1] = move
        grid_output(map)


def win_checker(map):
    print(map.get(1)[0] + " " + map.get(2)[1] + " " + map.get(3)[2])
    if map.get(1)[0] == map.get(2)[1] == map.get(3)[2] and map.get(1)[0] != " ":
        print(map.get(2)[1] + " wins")
        exit()
        return False
    if map.get(1)[2] == map.get(2)[1] == map.get(3)[0] and map.get(3)[0] != " ":
        print(map.get(2)[1] + " wins")
        exit()
        return False
    for x in map.keys():
        if map.get(x)[0] == map.get(x)[1] == map.get(x)[2] and map.get(x)[0] != " ":
            print(map.get(x)[0] + " wins")
            exit()
            return False
    for x in map.keys():
        if map.get(1)[x-1] == map.get(2)[x-1] == map.get(3)[x-1] and map.get(1)[x-1] != " ":
            print(map.get(1)[x-1] + " wins")
            exit()
            return False
    for x in map.keys():
        if map.get(x)[0] == " " or map.get(x)[1] == " " or map.get(x)[2] == " ":

            return True

    print("Draw")
    return False


def start_game(answer, map, coordinate_list):
    grid_output(map)
    while True:
        if answer[1] == "easy":
            easy_ai_move(map, "X")
        else:
            human_move(coordinate_list, map, "X")

        if answer[2] == "easy":
            easy_ai_move(map, "O")
        else:
            human_move(coordinate_list, map, "O")
        win_checker(cell_map)



start_game(first_input(), cell_map, coordinate_list)
grid_output(cell_map)