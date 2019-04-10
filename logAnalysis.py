#!/usr/bin/env python3
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

    select_q1 = """ SELECT count(path), path from log GROUP BY
                path ORDER BY count(path) DESC LIMIT 50 """
    cursor.execute(select_q1)
    records_toview = cursor.fetchall()
    slugs, views = [], []
    for i, record in enumerate(records_toview[1:4]):
        views.append(record[0])
        slugs.append(record[1].split('/')[-1].strip())
        print(f"\"{slugs[i]}\" -- {views[i]} views")
    for i, slug in enumerate(slugs):
        select_q2 = """ SELECT authors.name FROM authors INNER JOIN articles
        ON authors.id=articles.author WHERE articles.slug = (%s) """
        cursor.execute(select_q2, (slug, ))
        print(f'{cursor.fetchone()[0]} -- {views[i]} views')

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
