from game_ratings_analyzer import is_tie,read_ratings,normalize_path,generate_report
# python3 game_rating/game_ratings_analyzer.py game_rating/data/game_ratings.csv         
def test_is_tie():
    games = [('Stardew Valley', 10.0), ('Counter-Strike 2', 10.0), ('aaa',10.0)]
    assert is_tie(games)


def test_read_rating():
    
    path = "/home/intel/repo/d008py-bughunt-f2janyway/game_rating/data/game_ratings.csv"
    ratings = read_ratings(path)
    print("ratings")
    print(ratings)


# def test_normalize_path():
#     # case1 : path is other type 
#     # path = 1 
#     # path.replace("\\", "/")
#     # rs = normalize_path(path)

#     path = "\\\a\\"
#     import regex 
#     hex(0x01)
#     rs = path.replace("\\", "/")
#     assert rs == "/a/"

def test_read_rating_wrong_file_path():
    read_ratings("12")


# def test_normalize_path():
#     path = "\\\\\d\\\s\\\s\\\\\s"
#     assert normalize_path(path) == "/d/s/s/s"


def test_sort():
    
    rating = {12:"aaa", 13:"1212" }
    generate_report(ratings=rating,top_n=2)
    good_rating = {"aaa":[1], "bbb":[2]}
    generate_report(good_rating,2)

    
