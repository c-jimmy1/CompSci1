import json

def lowercase_genres(movies):
    """Change all genre strings in each movie's 'genre' list to lowercase."""
    for movie_id in movies:
        lowered = [g.lower() for g in movies[movie_id]['genre']]
        movies[movie_id]['genre'] = lowered


def compute_weighted_ratings(movies, ratings, min_year, max_year, w1, w2):
    """ Combined rating = (w1 * imdb_rating + w2 * average_twitter_rating) / (w1 + w2) """
    movie_ratings = {}

    for movie_id, info in movies.items():
        year = info['movie_year']
        imdb_rating = info['rating']

        # Check if movie has enough Twitter ratings
        if movie_id not in ratings or len(ratings[movie_id]) < 3:
            continue

        # Check if within requested year range
        if not (min_year <= year <= max_year):
            continue

        twitter_vals = ratings[movie_id]
        avg_twitter_rating = sum(twitter_vals) / len(twitter_vals)

        combined_rating = (w1 * imdb_rating + w2 * avg_twitter_rating) / (w1 + w2)
        movie_ratings[movie_id] = combined_rating

    return movie_ratings


def find_best_and_worst_in_genre(genre, movie_ratings, movies):
    """Given a genre string, a dictionary of { movie_id: combined_rating },
    and the original movies dictionary"""
    genre = genre.lower()
    filtered = []

    for movie_id, rating in movie_ratings.items():
        if genre in movies[movie_id]['genre']:
            filtered.append((rating, movie_id))

    if not filtered:
        return None, None

    # Sort descending by rating, then by movie_id if there's a tie
    filtered.sort(reverse=True, key=lambda x: (x[0], x[1]))

    # Best is the first item, worst is the last item
    best_id = filtered[0][1]
    worst_id = filtered[-1][1]
    return best_id, worst_id


def main():
    # Load data
    movies = json.loads(open("movies.json").read())
    ratings = json.loads(open("ratings.json").read())

    # Convert genres to lowercase
    lowercase_genres(movies)

    min_year = input('Min year => ').strip()
    print(min_year)
    min_year = int(min_year)

    max_year = input('Max year => ').strip()
    print(max_year)
    max_year = int(max_year)

    w1 = input('Weight for IMDB => ').strip()
    print(w1)
    w1 = float(w1)

    w2 = input('Weight for Twitter => ').strip()
    print(w2)
    w2 = float(w2)


    movie_ratings = compute_weighted_ratings(movies, ratings, min_year, max_year, w1, w2)

    while True:
        genre = input("\nWhat genre do you want to see? ").strip()
        print(genre)

        if genre.lower() == "stop":
            break

        best_id, worst_id = find_best_and_worst_in_genre(genre, movie_ratings, movies)

        if best_id is None and worst_id is None:
            # No movies found
            print("\nNo {} movie found in {} through {}".format(
                genre.title(), min_year, max_year
            ))
        else:
            # We have a best and worst
            best_rating = movie_ratings[best_id]
            worst_rating = movie_ratings[worst_id]
            print("\nBest:")
            print("        Released in {}, {} has a rating of {:.2f}".format(
                movies[best_id]['movie_year'],
                movies[best_id]['name'],
                best_rating
            ))
            print("\nWorst:")
            print("        Released in {}, {} has a rating of {:.2f}".format(
                movies[worst_id]['movie_year'],
                movies[worst_id]['name'],
                worst_rating
            ))


if __name__ == "__main__":
    main()
