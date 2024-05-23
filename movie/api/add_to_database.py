import json

with open('kinopoisk.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


def get_actors():
    counter = 0
    result = []
    all_actors = []
    names_actors = []
    for item in data:
        actors = [{"name": i.get("name"), "photo": i.get("photo")} for i in item["persons"] if i["enProfession"] == "actor" and i.get("name") is not None]
        all_actors.extend(actors)

    for i in range(len(all_actors)):
        main = {"model": "movie.Actor", "pk": counter + 1, "fields": all_actors[i] if all_actors[i]["name"] not in names_actors else print(0)}
        if main["fields"] is not None:
            result.append(main)
        counter += 1

        names_actors.append(all_actors[i]["name"])

        with open("../../fixtures/actors_fixtures.json", "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)


def get_movies():
    counter = 0

    with open("../../fixtures/actors_fixtures.json", 'r', encoding='utf-8') as f:
        fix_actor = json.load(f)

    result = []
    for item in data:
        title = item["name"]
        genre = [i["name"] for i in item["genres"]]
        release_year = item["year"]
        director = [i.get("name") for i in item["persons"]
                    if i["enProfession"] == "director" and i.get("name") is not None]
        duration = f'{item["movieLength"] // 60}ч. {item["movieLength"] % 60}мин.'
        age_rating = item.get("ageRating", "Не указано")
        country = [i["name"] for i in item["countries"]]
        actors = [i.get("name") for i in item["persons"] if i["enProfession"] == "actor" and i.get("name") is not None]
        description = item["description"]
        rating = int(item["rating"]["kp"])
        price = 0
        poster = item["poster"]["url"]
        trailer = item.get("videos")["trailers"][0]["url"] \
            if item.get("videos") and len(item.get("videos").get("trailers")) >= 1 else None

        print(actors)
        # ЗАПИСЫВАЕМ ID АКТЕРОВ ДЛЯ СВЯЗИ С ФИЛЬМАМИ
        index_actors = []
        for i in actors:
            for act in fix_actor:
                if act["fields"] is not None:
                    if act["fields"]["name"] == i:
                        index_actors.append(int(act["pk"]))
                    else:
                        continue

        # ЗАПИСЫВАЕМ ЖАНРЫ КАК СТРОКУ
        str_genre = ""
        counter_genre = 1
        for i in genre:
            if counter_genre == len(genre):
                str_genre += i
            elif len(genre) > 1:
                str_genre += i + ", "
            else:
                str_genre += i
            counter_genre += 1

        # ЗАПИСЫВАЕМ РЕЖИССЕРОВ КАК СТРОКУ
        str_director = ""
        counter_director = 1
        for i in director:
            if counter_director == len(director):
                str_director += i
            elif len(director) > 1:
                str_director += i + ", "
            else:
                str_director += i
            counter_director += 1

        # ЗАПИСЫВАЕМ СТРАНЫ КАК СТРОКУ
        str_country = ""
        counter_country = 1
        for i in country:
            if counter_country == len(country):
                str_country += i
            elif len(country) > 1:
                str_country += i + ", "
            else:
                str_country += i
            counter_country += 1

        main = {"model": "movie.Movie", "pk": counter + 1, "fields": {
            "title": title,
            "genre": str_genre,
            "release_year": release_year,
            "director": str_director,
            "duration": duration,
            "age_rating": str(age_rating) + "+" if age_rating else age_rating,
            "country": str_country,
            "actors": index_actors,
            "description": description,
            "rating": rating,
            "price": price,
            "poster": poster,
            "trailer": trailer
        }}

        result.append(main)
        counter += 1
        with open("../../fixtures/movies_fixtures.json", "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)


get_actors()
get_movies()
