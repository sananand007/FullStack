#!/usr/bin/env python3.6
"""Log Analysis project"""

import psycopg2

try:
    connection = psycopg2.connect(user="postgres", password="postgres",
                                  host="127.0.0.1",
                                  port="5432", database="news")
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print(f"you are connected to - {record}")
    select_q1 = """ SELECT title, count (*) AS views
                    FROM articles
                    INNER JOIN log
                    ON log.path = '/article/' || articles.slug
                    GROUP BY title
                    ORDER BY views DESC
                    LIMIT 3 """
    cursor.execute(select_q1)
    records_toview = cursor.fetchall()
    for title, views in records_toview:
        print(f"\"{title}\" -- {views} views")
    select_q2 = """ SELECT authors.name, views
                    FROM authors
                    JOIN (
                    SELECT sub.author, views
                    FROM
                    (
                        SELECT author, count(*) AS views
                        FROM articles
                        INNER JOIN log
                        ON log.path = '/article/' || articles.slug
                        GROUP BY author
                        ORDER BY views DESC
                        LIMIT 3
                    ) sub
                    ) sub2
                    ON sub2.author=authors.id;
            """
    cursor.execute(select_q2)
    for author, views in cursor.fetchall():
        print(f"{author} -- {views} views")
    # Just test database log
    select_q3 = """ SELECT  count(status) from log ; """
    cursor.execute(select_q3)
    count_res = int(cursor.fetchall()[0][0])
    select_q3_h = """ SELECT TO_CHAR(log.time :: DATE, 'Mon dd, yyyy')
            as date, log.status, Count(*) FROM
            log GROUP BY date, log.status """
    cursor.execute(select_q3_h)
    records = cursor.fetchall()
    for i in range(0, len(records), 2):
        val = round(float(int(records[i+1][-1]) /
                    (1.000 * (int(records[i][-1]) +
                              int(records[i+1][-1])))), 3)
        if val > 0.01:
            val *= 100
            print(f'{records[i][0]} --  {val}% errors')

except (Exception, psycopg2.Error) as error:
    print(error)
finally:
    # closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("connection closed !")
