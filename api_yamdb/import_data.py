import csv
import datetime as dt
import sqlite3


def import_category():
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    path = 'static/data/category.csv'
    with open(path, encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=",")
        for row in file_reader:
            data = [
                (row['id'],
                 row['slug'],
                 row['name']),
            ]
            table_name = 'reviews_category'
            try:
                cur.executemany(
                    f'INSERT INTO {table_name} VALUES(?,?,?);', data
                )
            except Exception as e:
                print(e.__class__, 'Ошибка импорта!')
    con.commit()
    con.close()


def import_comments():
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    path = 'static/data/comments.csv'
    with open(path, encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=",")
        for row in file_reader:
            data = [
                (row['id'],
                 row['text'],
                 row['pub_date'],
                 row['author'],
                 row['review_id']
                 ),
            ]
            print(data)
            table_name = 'reviews_comment'
            try:
                cur.executemany(
                    f'INSERT INTO {table_name} VALUES(?,?,?,?,?);', data
                )
            except Exception as e:
                print(e.__class__, 'Ошибка импорта!')
    con.commit()
    con.close()


def import_genre():
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    path = 'static/data/genre.csv'
    with open(path, encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=",")
        for row in file_reader:
            data = [
                (row['id'],
                 row['name'],
                 row['slug']
                 ),
            ]
            print(data)
            table_name = 'reviews_genre'
            try:
                cur.executemany(
                    f'INSERT INTO {table_name} VALUES(?,?,?);', data
                )
            except Exception as e:
                print(e.__class__, 'Ошибка импорта!')
    con.commit()
    con.close()


def import_genre_title():
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    path = 'static/data/genre_title.csv'
    with open(path, encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=",")
        for row in file_reader:
            data = [
                (row['id'],
                 row['genre_id'],
                 row['title_id']
                 ),
            ]
            print(data)
            table_name = 'reviews_genretitle'
            try:
                cur.executemany(
                    f'INSERT INTO {table_name} VALUES(?,?,?);', data
                )
            except Exception as e:
                print(e.__class__, 'Ошибка импорта!')
    con.commit()
    con.close()


def import_review():
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    path = 'static/data/review.csv'
    with open(path, encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=",")
        for row in file_reader:
            data = [
                (row['id'],
                 row['pub_date'],
                 row['text'],
                 row['score'],
                 row['author'],
                 row['title_id'],
                 ),
            ]
            print(data)
            table_name = 'reviews_review'
            try:
                cur.executemany(
                    f'INSERT INTO {table_name} VALUES(?,?,?,?,?,?);', data
                )
            except Exception as e:
                print(e.__class__, 'Ошибка импорта!')
    con.commit()
    con.close()


def import_titles():
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    path = 'static/data/titles.csv'
    with open(path, encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=",")
        for row in file_reader:
            data = [
                (row['id'],
                 row['name'],
                 row['category'],
                 None,  # description
                 1,  # rating
                 row['year'],
                 ),
            ]
            print(data)
            table_name = 'reviews_title'
            try:
                cur.executemany(
                    f'INSERT INTO {table_name} VALUES(?,?,?,?,?,?);', data
                )
            except Exception as e:
                print(e.__class__, 'Ошибка импорта!', e)
    con.commit()
    con.close()


def import_users():
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    path = 'static/data/users.csv'
    with open(path, encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=",")
        for row in file_reader:
            print(row)
            data = [
                (row['id'],
                 '1234PassWord',
                 dt.date.today(),
                 False,
                 row['username'],
                 row['first_name'],
                 row['last_name'],
                 row['email'],
                 False,
                 True,
                 dt.date.today(),
                 row['bio'],
                 1234,
                 row['role'],

                 ),
            ]
            print(data)
            table_name = 'reviews_user'
            try:
                cur.executemany(
                    f'INSERT INTO {table_name} VALUES('
                    f'?,?,?,?,?,?,?,?,?,?,?,?,?,?);',
                    data
                )
            except Exception as e:
                print(e.__class__, 'Ошибка импорта!', e)
    con.commit()
    con.close()


def main():
    import_category()
    import_comments()
    import_genre()
    import_genre_title()
    import_review()
    import_titles()
    import_users()


if __name__ == '__main__':
    main()
