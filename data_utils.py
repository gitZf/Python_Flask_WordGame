# data_utils.py - part of the WordGame - by Paul Barry.
# email: paul.barry@itcarlow.ie


#import DBcm
import mysql.connector

config = {
    'host': '127.0.0.1',
    'user': 'zoltan',
    'password': '*********',
    'database': 'wordgameDB',
}


def add_to_scores(name: str, score: float, sourceword: str) -> None:
    """Add the name and its associated score to the pickle."""
    _SQL = """insert into leaderboard
              (name, score, sourceword)
              values
              (%s, %s, %s)"""
    with DBcm.UseDatabase(config) as cursor:
        cursor.execute(_SQL, (name, score, sourceword))
    

def get_sorted_leaderboard() -> list:
    """Return a sorted list of tuples - this is the leaderboard."""
    _SQL = """select score, name, sourceword from leaderboard
              order by score"""
    with DBcm.UseDatabase(config) as cursor:
        cursor.execute(_SQL)
        data = cursor.fetchall()
    return [(float(row[0]), row[1], row[2]) for row in data]
    # tempdata = []
    # for row in data:
    #     tempdata.append((float(row[0]), row[1], row[2]))
    # data = tempdata

