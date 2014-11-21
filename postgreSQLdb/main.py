"""
DB Benchmarking Application
===========================

Mongo_db.py

This file handles all interactions with MongoDB during the benchmarking
process.

"""

import psycopg2
import os

from local import *
from benchmark_template import BenchmarkDatabase


class Benchmark(BenchmarkDatabase):

    def __init__(self, collection, setup=False):

        if setup:
            self.setup(collection)

        self.conn = ''

    def setup(self, collection):
        """ This function will set up the connection with the DB.  The options
        used here are all configured in the config file.

        :param collection: The collection that all benchmark writes will happen
                    with

        """
        # #TODO - fix how the collection is used here
        #
        # self.client = MongoClient(host=MONGO_PRIMARY, port=MONGO_PORT)
        #
        # self.db = self.client.test
        #
        # self.collection = self.db.test_collection
        #
        # self.collection.ensure_index("Index")

        self.conn = psycopg2.connect(
            host=POSTGRESQL_1,
            port=POSTGRESQL_PORT,
            user=POSTGRESQL_USER,
            password=POSTGRESQL_PASSWORD,
            dbname=collection,
        )

        self.cur = self.conn.cursor()

        lock_file = 'sql.lock'
        dir = 'postgreSQLdb'
        file_list = os.listdir(dir)

        if lock_file in file_list:

            delete = 'DROP TABLE {table} cascade'.format(table=collection)

            self.cur.execute(delete)

        else:

            with open('{dir}/{lock}'.format(lock=lock_file, dir=dir,), 'w+'):
                pass


        create_table = 'CREATE TABLE test ' \
                       '({index}, {number}, {info});'.\
            format(
                index='Index int',
                number='Number int',
                info='Info text',
            )

        self.cur.execute(create_table)

        self.commit()

    def write(self, data):
        """ The function handles all writes with MongoDB.  It takes a single
        parameter (a dict of sample data) and then writes it to the DB.

        :param data: An incoming dict that will be written to the DB

        """

        insert = 'INSERT INTO test (Index, Number, Info) VALUES ({Index}, ' \
                 '{Number}, {Info!r});'.format(**data)

        self.cur.execute(insert)

        self.commit()


    def read(self, index):
        """ This function handles all reads from MongoDB.  It takes a single
        parameter (index) which determines which record to retrieve from the DB.

        :param index: The index of the record to be retrieved from the DB

        :return read_entry: the entry retrieved from the DB

        """

        select = 'SELECT * from test WHERE Index = {index};'.format(index=index)

        self.cur.execute(select)
        return self.cur.fetchone()

    def commit(self):
        """ Commits the current transaction.  This function is ONLY USED FOR
        SQL-TYPE DATABASES.

        :return:
        """

        self.cur.execute('commit;')

        # query = {
        #     'Index': index
        # }
        #
        # read_entry = self.collection.find_one(query)
        #
        # return read_entry
