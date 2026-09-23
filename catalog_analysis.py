import math

movies = [
    {
        "title": "The Dune Chronicles", 
        "year": 2021, 
        "genres": {"sci-fi", "drama"},
        "rating": 8.6, 
        "duration_min": 155, 
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]
    },
    {
        "title": "Kitchen Stories", 
        "year": 2019, 
        "genres": {"comedy", "drama"},
        "rating": 7.1, 
        "duration_min": 98, 
        "actors": ["A. Novak", "M. Ferguson"]
    },
    {
        "title": "silent hours", 
        "year": 2016, 
        "genres": {"thriller", "drama"}, 
        "rating": 6.4, 
        "duration_min": 112, 
        "actors": ["J. Bloom", "K. Lee"]
    },
    {
        "title": "Comet Racers", 
        "year": 2023, 
        "genres": {"sci-fi", "action"}, 
        "rating": 5.9, 
        "duration_min": 101, 
        "actors": ["O. Isaac", "P. Diaz"]
    },
    {
        "title": "The Last Bakery", 
        "year": 2014, 
        "genres": {"comedy"}, 
        "rating": 7.8, 
        "duration_min": 89, 
        "actors": ["A. Novak", "T. Chalamet"]
    },
    {
        "title": "midnight in oslo", 
        "year": 2020, 
        "genres": {"thriller", "mystery"}, 
        "rating": 8.9, 
        "duration_min": 124, 
        "actors": ["K. Lee", "R. Ferguson"]
    },
    {
        "title": "Garden of Static", 
        "year": 2022, 
        "genres": {"drama"}, 
        "rating": 4.8, 
        "duration_min": 137, 
        "actors": ["P. Diaz", "J. Bloom"]
    },
    {
        "title": "The Quiet Algorithm", 
        "year": 2024, 
        "genres": {"sci-fi", "drama"}, 
        "rating": 9.2, 
        "duration_min": 118, 
        "actors": ["M. Ferguson", "O. Isaac"]
    },
    {
        "title": "Two Left Shoes", 
        "year": 2011, 
        "genres": {"comedy"},
        "rating": 6.0, 
        "duration_min": 95, 
        "actors": ["A. Novak", "K. Lee"]
    },
    {
        "title": "Red Harbor", 
        "year": 2018, 
        "genres": {"action", "thriller"}, 
        "rating": 7.3, 
        "duration_min": 129, 
        "actors": ["P. Diaz", "T. Chalamet"]
    },
]

# Этап 1. Разминка: переменные, числа, math

def average_rating(movies):
    sum_rating = 0
    count = 0

    for i in range(len(movies)):
        sum_rating += movies[i]["rating"]
        count += 1
    avg_rating = sum_rating / count

    return round(avg_rating, 1)

def catalog_age_stats(movies, current_year=2026):
    years = []

    for i in range(len(movies)):
        years.append(movies[i]["year"])

    oldest_age = current_year - min(years)
    newest_age = current_year - max(years)
    average_age = current_year - (sum(years) / len(years))

    return (oldest_age, newest_age, math.ceil(average_age))

def duration_in_hours(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f"{hours}ч {remaining_minutes}м"


# Этап 2. Условия и match

def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    return "средне" if rating >= 5 else "слабо"

def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"


# Этап 3. Циклы

# По условию этапа 3 оба цикла содержат вывод через print.
# Чтобы демонстрационный вывод не выполнялся при каждом запуске программы,
# циклы объединены в функцию demonstrate_loops().
# Функция сохраняет требуемые for/continue и while/break/else,
# но вызывается только при необходимости.

def demonstrate_loops(movies):
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])

    i = 0
    while i < len(movies):
        if movies[i]["rating"] > 9.0:
            print(movies[i]["title"])
            break
        i += 1
    else:
        print("Шедевров не найдено")

def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


# Этап 4. Строки

def normalize_title(title):
    words = title.split()
    normalized_words = []

    for word in words:
        normalized_word = word[0].upper() + word[1:]
        normalized_words.append(normalized_word)

    return " ".join(normalized_words)

def make_slug(title):
    return title.lower().replace(" ", "-")

def format_report_line(movie):
    title = normalize_title(movie["title"])
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))

    return (
        f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, '
        f'{duration}, жанры: {genres}'
    )

# Этап 5. Списки

def titles_sorted_by_rating(movies):
    sorted_movies = sorted(
        movies,
        key=lambda movie: movie["rating"],
        reverse=True)

    titles = []
    for movie in sorted_movies:
        titles.append(movie["title"])

    return titles

def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(
        movies,
        key=lambda movie: movie["rating"],
        reverse=True)

    top_movies = []
    for movie in sorted_movies[:n]:
        top_movies.append((movie["title"], movie["rating"]))

    return top_movies


# Этап 6. Словари

def count_by_genre(movies):
    genre_counts = {}

    for movie in movies:
        for genre in movie["genres"]:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1

    return genre_counts

def actor_filmography(movies):
    filmography = {}

    for movie in movies:
        for actor in movie["actors"]:
            if actor not in filmography:
                filmography[actor] = []
            filmography[actor].append(movie["title"])
    
    return filmography

average = average_rating(movies)
above_average_ratings = {
    movie["title"]: movie["rating"]
    for movie in movies
    if movie["rating"] > average}


# Этап 7. Множества

def all_genres(movies):
    genres = set()
    for movie in movies:
        genres.update(movie["genres"])
    return genres

def common_actors(movie1, movie2):
    actors_1 = set(movie1["actors"])
    actors_2 = set(movie2["actors"])
    return actors_1 & actors_2

def genres_only_in_one(movies_a, movies_b):
    genres_a = all_genres(movies_a)
    genres_b = all_genres(movies_b)
    return genres_a - genres_b

# Этап 8. Итераторы и генераторы

def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie

# По условию этапа 8 работа генератора демонстрируется через print.
# Чтобы этот вывод не выполнялся при каждом запуске программы,
# демонстрационный цикл вынесен в отдельную функцию.

def demonstrate_high_rated(movies):
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))

# Генераторное выражение

total_duration = sum(
    movie["duration_min"]
    for movie in movies
    if movie["rating"] > 7)