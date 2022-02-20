import mysql.connector
import Const

class TrainingDataAccess:

    def __init__(self):
        my_sql_object = mysql.connector.connect(
            host="localhost",
            user="root",
            password=Const.DBPASSWORD,
            database="stocktickers"
        )
        cursor = my_sql_object.cursor()

    def get_training_data(self):
        
        return