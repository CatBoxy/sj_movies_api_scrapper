
import mysql.connector
from mysql.connector import Error


class DB():
    def __init__(self, db):
        try:
            self.connection = mysql.connector.connect(
                port="3306",
                host="127.0.0.1",
                user="root",
                password="2154625",
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
            values = []
            query = "INSERT INTO {tabla} ({namesString}) VALUES ({placeholdersString})".format()
            cursor = self.connection.cursor()
            cursor.execute(query, values)
        except Error as ex:
            print('Error al crear: {0}'.format(ex))

