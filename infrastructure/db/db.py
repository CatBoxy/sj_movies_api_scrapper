from typing import Optional

import mysql.connector
from mysql.connector import Error


class DB():
    def __init__(self, db, password):
        try:
            self.connection = mysql.connector.connect(
                port="3306",
                host="127.0.0.1",
                user="root",
                password=password,
                db=db
            )
            self.cursor = self.connection.cursor()
            print('coneccion establecida')
        except Error as ex:
            print('Error al conectar: {0}'.format(ex))

    def initTransaction(self):
        try:
            self.connection.start_transaction()
        except Error as ex:
            print('Error al iniciar transaccion: {0}'.format(ex))

    def commit(self):
        try:
            self.connection.commit()
        except Error as ex:
            print('Error al ejecutar commit: {0}'.format(ex))

    def rollback(self):
        try:
            print('Ejecutando rollback')
            self.connection.rollback()
        except Error as ex:
            print('Error al ejecutar rollback: {0}'.format(ex))

    def deleteAll(self, tabla):
        try:
            query = "DELETE FROM {tabla}".format(tabla=tabla)
            cursor = self.connection.cursor()
            cursor.execute(query)
        except Error as ex:
            print('Error al eliminar valores: {0}'.format(ex))

    def insert(self, tabla, fields: dict):
        try:
            placeholders = ()
            values = tuple(dict.values(fields))
            fieldNames = tuple(dict.keys(fields))

            for name in fields:
                placeholders = (*placeholders, "%s")

            namesString = ', '.join(fieldNames)
            placeholdersString = ', '.join(placeholders)

            query = "INSERT INTO {tabla} ({namesString}) VALUES ({placeholdersString})".format(tabla=tabla,
                                                                                               namesString=namesString,
                                                                                               placeholdersString=placeholdersString)
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            self.connection.commit()
        except Error as ex:
            print('Error al insertar: {0}'.format(ex))

    def select(self, query, values: Optional[tuple] = None):
        try:
            cursor = self.connection.cursor()
            if values is None:
                cursor.execute(query)
            else:
                cursor.execute(query, values)
            columnNames = cursor.column_names
            allRows = cursor.fetchall()
            rowsFound = []

            for row in allRows:
                if len(columnNames) == len(row):
                    rowsFound.append({columnNames[i]: row[i] for i, _ in enumerate(row)})

            return rowsFound
        except Error as ex:
            print('Error al buscar: {0}'.format(ex))