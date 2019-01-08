def command_menu():
   print("COMMAND MENU")
   print("list - List all movies")
   print("add  - Add a movie")
   print("del  - Delete a movie")
   print("exit - Exit program")
   print()


def list_movies(movie_list):
    if len(movie_list) == 0:
        print("There are no movies in the list.\n")
    else:
        i = 1
        for row in movie_list:
            print(f"{i}. {row[0]} ({row[1]})")
            i += 1
        print()

def add_movie(movie_list):
    name = input("Name: ")
    year = input("Year: ")

    movie = [name, year]
    movie_list.append(movie)
    print(f"{movie[0]} was added.\n")


def del_movie(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number - 1)
        print(f"{movie[0]} was deleted.\n")
    print()


def main():
    movie_list = [["Mulan", 1998],
                  ["Pocahantas", 1994],
                  ["Moana", 2016]]

    command_menu()

    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list_movies(movie_list)
        elif command.lower() == "add":
            add_movie(movie_list)
        elif command.lower() == "del":
            del_movie(movie_list)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.")

    print("Bye!")


if __name__ == "__main__":
    main()