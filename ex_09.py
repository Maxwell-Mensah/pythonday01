def print_movie_from_nbr(nbr):
    match nbr:
        case 3:
            print("The Three Brothers")
        case 6:
            print("The Sixth Sense")
        case 23:
            print("The Nulber 23")
        case 28:
            print("28 Days Later")
        case _:
            print("I don't know")


print_movie_from_nbr(655)