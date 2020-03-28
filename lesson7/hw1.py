def favorite_movie(film_name):
    return f"My favorite movie is named {film_name}"

if __name__ == "__main__":
    film = input("Какой ваш любимый фильм? ")
    print(favorite_movie(film))