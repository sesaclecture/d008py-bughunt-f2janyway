import sys
import csv


# def normalize_path(path):
    # if type(path) is str:
    #     return path.replace("\\", "/")
    

    #origin
    # return path.replace('\\', "/")
def normalize_path(path):
    rep_path = path
    while "\\" in rep_path or "//" in rep_path:
        rep_path = rep_path.replace('\\',"/").replace('//','/')
    return rep_path
    


def is_valid_rating(r):
    return 0 <= r <= 10

def is_tie(games):

    print(games)
    print("22222222")
    print(games[0][1])
    print("22222222")
    print(games[-1][1])
    # return games[0][1] == games[-1][1]

    before_value = games[0][1]
    for tu in games:
        if before_value != tu[1]:
            return False
        before_value = tu[1] 

    return True
        


def read_ratings(file_path):
    ratings = {}
    try:
        with open(file_path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # 컬럼이 없는 경우
                # keys = row.keys()
                # if "title" in keys and "rating" in keys:
                #     print(f"row:{row}")
                #     title = row["title"]
                #     # int가 아닌 경우, 공백?
                #     try:
                #         rating = int(row["rating"])
                #         if title in ratings:
                #             ratings[title].append(rating)
                #         else:
                #             ratings[title] = [rating]
                #     except ValueError as e:
                #         print("rating is not int")

                # origin
                title = row["title"]
                rating = int(row["rating"])
                if title in ratings:
                    ratings[title].append(rating)
                else:
                    ratings[title] = [rating]
        return ratings
    except FileNotFoundError:
        pass


def generate_report(ratings, top_n):
    averages = {}
    # print(ratings)
    for key, value in ratings.items():
        if type(key) is str and type(value) is list:
            break
        else:
            # raise ValueError
            return

    
    for title, scores in ratings.items():
    
        averages[title] = sum(scores) / len(scores)

    sorted_games = sorted(averages.items(), key=lambda x: x[1], reverse=True)

    for i in range(top_n):
        title, avg = sorted_games[i]
        print(f"{i+1}. {title} - Avg Rating: {avg:.2f}")

    if is_tie(sorted_games):
        print("All games have the same average rating.")


def main(path):
    file_path = normalize_path(path)
    print("file_path")
    print(file_path)
    print()
    ratings = read_ratings(file_path)
    generate_report(ratings, 10)


if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except IndexError:
        print(f"사용법: {sys.argv[0]} <입력 CSV 파일>")
