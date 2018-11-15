import psycopg2

DATABASE_NAME = 'news'


def query(sql):
    conn = psycopg2.connect(database=DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    conn.close()
    return results


def the_most_three_articles():
    query_the_most_three_articles = '''select articles.title, count(*) as number
                from log, articles
                where log.status='200 OK'
                and articles.slug = substr(log.path, 10)
                group by articles.title
                order by number desc
                limit 3;'''
    results = query(query_the_most_three_articles)
    print("What are the most popular three articles of all time?")

    # print the result
    for title, number in results:
        print("\"{}\" -- {} views".format(title, number))


def the_most_popular_article_authors():
    query_the_most_popular_article_authors = '''select authors.name, count(*) as number
                from articles, authors, log
                where log.status='200 OK'
                and authors.id = articles.author
                and articles.slug = substr(log.path, 10)
                group by authors.name
                order by number desc;
                '''
    results = query(query_the_most_popular_article_authors)
    print("\nWho are the most popular article authors of all time?")

    # print the result
    for name, number in results:
        print("{} -- {} views".format(name, number))


def more_one_percentage_lead_to_error():
    query_more_one_percentage_lead_to_error = '''WITH all_requests AS (
                SELECT time::date AS day, count(*)
                FROM log
                GROUP BY time::date
                ORDER BY time::date
              ), error_requests AS (
                SELECT time::date AS day, count(*)
                FROM log
                WHERE status != '200 OK'
                GROUP BY time::date
                ORDER BY time::date
              ), error_rate AS (
                SELECT all_requests.day,
                  round(((error_requests.count*100.0)/all_requests.count*1.0), 2)
                  AS percent
                FROM all_requests, error_requests
                WHERE all_requests.day = error_requests.day
              )
            SELECT * FROM error_rate WHERE percent > 1;  
                '''

    results = query(query_more_one_percentage_lead_to_error)
    print("\nOn which days did more than 1% of requests lead to errors")

    # print the result
    for result in results:
        print('{date:%b %d,%Y} -- {error_rate:.2f}%'.format(
            date=result[0],
            error_rate=result[1]))


# Question #1
the_most_three_articles()
# Question #2
the_most_popular_article_authors()
# Question #3
more_one_percentage_lead_to_error()
