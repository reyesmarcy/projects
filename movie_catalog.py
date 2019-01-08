#! /usr/bin/env python3

def display_menu():
    print("The Movie Catalog Program")
    print()
    print("Menu")
    print("actor - List Movies for Actor")
    print("list  - Show All Movie by Title")
    print("show  - Show Movie Info")
    print("add   - Add Movie")
    print("edit  - Edit Movie Info")
    print("del   - Delete Movie")
    print("exit  - Exit Program")


def show_movie(movie_catalog):
    title = input("Enter the title for the movie: ")
    if title in movie_catalog:
        movie = movie_catalog[title]
        print("Title:        " + title)
        print("Lead Actor:   " + movie["actor"])
        print("Release Year: " + movie["year"])
    else:
        print("The movie does not exist in the catalog.")


def add_edit_movie(movie_catalog, mode):
    title = input("Enter the title for the movie: ")
    if mode == "add" and title in movie_catalog:
        print(title + " already exists in the catalog.")
        response = input("Would you like to edit movie? (y/n): ").lower()
        if response != "y":
            return
    elif mode == "edit" and title not in movie_catalog:
        print(title + " does not exist in the catalog.")
        response = input("Would you like to add movie? (y/n): ").lower()
        if response != "y":
            return

    actor = input("Enter the actor name: ")
    year = input("Enter release year: ")
    movie = {"actor": actor, "year": year}

    movie_catalog[title] = movie


def del_movie(movie_catalog):
    title = input("Enter the title for the movie: ")
    if title in movie_catalog:
        del movie_catalog[title]
        print(title + " has been removed from the catalog.")
    else:
        print("The movie does not exist in the catalog.")


def list_movie(movie_catalog):
    print("The Movie Catalog Listing")
    print("-------------------------")
    for code in movie_catalog.keys():
        print(code)


def list_actor(movie_catalog):
    actor = input("Enter Actor: ")
    for key, value in movie_catalog.items():
        if actor == movie_catalog[key]["actor"]:
            print(key)


def main():
    movie_catalog = {
        "Big":
            {"actor": "Tom Hanks",
             "year": "1988"},
        "Toy Story":
            {"actor": "Tim Allen",
             "year": "1994"},
        "Man on Fire":
            {"actor": "Denzel Washington",
             "year": "2004"}
    }

    display_menu()

    while True:
        print()
        command = input("Command: ").lower()
        if command == "show":
            show_movie(movie_catalog)
        elif command == "add":
            add_edit_movie(movie_catalog, mode="add")
        elif command == "edit":
            add_edit_movie(movie_catalog, mode="edit")
        elif command == "del":
            del_movie(movie_catalog)
        elif command == "list":
            list_movie(movie_catalog)
        elif command == "actor":
            list_actor(movie_catalog)
        elif command == "exit":
            print("That's all folks!")
            break
        else:
            print("Not a valid command. Try again.")


if __name__ == "__main__":
    main()


