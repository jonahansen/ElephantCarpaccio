import mysql.connector

class Repository(object):
    mydatabase = object
    mycursor = object
    RowsList = []

    def __init__(self):
        pass
    
    # to set connection up as student user on dk1studentuser
    def Connect2DB(self):
        self.mydatabase = mysql.connector.connect(
                  host = "localhost",
                  user = "root",
                  password = "Jona6286",
                  database = "skatteoversigt"
                  )
        self.mycursor = self.mydatabase.cursor()

    # to get all table elements as a list
    def GetTableElements(self, tableName):   
        self.mycursor.execute("select * from skatteoversigt.%s" %tableName)
        RowsList = self.mycursor.fetchall()
        return RowsList
    
    def InsertDiscount(self, disBase, disValue):
        discount = [(disBase,disValue),(disBase,disValue)]
        self.mycursor.execute("insert into discountTable (discountInterval,discountValue) values (%s,%s)", (disBase, disValue))
        self.mydatabase.commit()

