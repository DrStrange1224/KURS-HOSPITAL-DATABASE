import psycopg2
import psycopg2.pool
from configparser import ConfigParser as cp
from contextlib import contextmanager
from mycp import *

class DBParser:
    """
    Static class
    """
    conn = None
    cur = None

    def init(iniFilePath:str, section:str):
        params = get_config(iniFilePath,section)
        __class__.dbpool = psycopg2.pool.ThreadedConnectionPool(
            minconn=1,
            maxconn=1,
            **params)
        __class__.conn = __class__.dbpool.getconn()
        __class__.cur = __class__.conn.cursor()

    def execute(sqlquery:str) -> list:
        """
        Returns list of tuples (rows)
        """
        try:
            __class__.cur.execute(sqlquery)
            res = __class__.cur.fetchall()
            __class__.conn.commit()
            return res
        except:
            __class__.conn.rollback()
            raise
    


    # @contextmanager
    # def db_cursor(self):
    #     self.conn = self.dbpool.getconn()
    #     try:
    #         with self.conn.cursor() as cur:
    #             yield cur
    #             self.conn.commit()
    #     # You can have multiple exception types here.
    #     # For example, if you wanted to specifically check for the
    #     # 23503 "FOREIGN KEY VIOLATION" error type, you could do:
    #     # except psycopg2.Error as e:
    #     #     conn.rollback()
    #     #     if e.pgcode = '23503':
    #     #         raise KeyError(e.diag.message_primary)
    #     #     else
    #     #         raise Exception(e.pgcode)
    #     except:
    #         self.conn.rollback()
    #         raise
    #     finally:
    #         self.dbpool.putconn(self.conn)