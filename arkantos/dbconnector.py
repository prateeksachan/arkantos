import psycopg2
import sys
from psycopg2.extras import NamedTupleConnection


class DbConnector:

    @classmethod
    def get_db_connection(cls, database: str, user: str, password: str, host: str, port: int):
        """
        create a postgres DB connection

        :param str database: database name
        :param str user: database user name
        :param str password: database user password
        :param str host: postgres host
        :param int port: postgres port

        :rtype: object
        :return: connection object
        """
        try:
            connection = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
            return connection
        except:
            sys.exit("could not connect to database: '{}'".format(database))

    @classmethod
    def get_cursor_from_connection(cls, connection):
        """
        postgres cursor

        :param object connection: database connection object

        :rtype: object
        :return: connection cursor object
        """
        return connection.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)

    @classmethod
    def get_data(cls, cur, query):
        """
        execute query and return records

        :param object cur: database connection cursor
        :param str query: database query

        :rtype: list
        :return: list of records fetched by the query
        """
        cur.execute(query)
        rows = cur.fetchall()
        return [dict(row._asdict()) for row in rows]
