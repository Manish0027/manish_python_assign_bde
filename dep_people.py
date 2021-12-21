import psycopg2


def manish_return_dep_people(organazation_id):
    con = None
    try:
        con = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="MYdell027",
            database="as1_db")

        cur = con.cursor()
        cur.callproc('test_sch.manish_return_dep_people', (organazation_id,))
        row = cur.fetchone()
        while row is not None:
            data = row
            row = cur.fetchone()

        cur.close()
    except(Exception, psycopg2.DataError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()
    return