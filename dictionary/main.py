import ast


def read_from_file(filename):
    faceit_dict = []
    with open(filename, "r") as r:
        for n, line in enumerate(r):
            line = line.strip()
            faceit_player = ast.literal_eval(line)
            faceit_dict.append(faceit_player)
            #print(faceit_player)

    if faceit_dict:
        return faceit_dict
    raise IndexError("File is empty.")

def more_than_avg_lvl(faceit_dict):
    more_than_avg_player = []
    for curr_dict in faceit_dict:
        player_elo = curr_dict["elo"]
        if player_elo >= 950:
            more_than_avg_player.append(curr_dict)
    if more_than_avg_player:
        return more_than_avg_player
    raise ValueError("All players are below average.")

def print_dict(faceit_dict):
    for faceit_player in faceit_dict:
        print(faceit_player)

def print_nick_and_elo(faceit_dict):
    for curr_dict in faceit_dict:
        curr_dict.pop("lvl")
    print_dict(faceit_dict)


if __name__ == "__main__":

    try:
        faceit_dict = read_from_file("dict.txt")
    except Exception as e:
        print(e)
        exit(0)
    except IndexError:
        print("Hello")
        exit(0)
    try:
        avg_players = more_than_avg_lvl(faceit_dict)
    except Exception as e:
        print(e)
        exit(0)
    print("All Players:")
    print_dict(faceit_dict)
    print("Avg Players:")
    print_dict(avg_players)

    print("Nick & Elo:")
    print_nick_and_elo(faceit_dict)


