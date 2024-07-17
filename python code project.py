import mysql.connector
import serial
import time
import string

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="dbserial"
)

device='COM3'
pieces=[]

a=1
while(a<=15):
    try:
        print("Trying...",device)
        arduino=serial.Serial(device,9600)
    except:
        print("Failed to connect ",device)

    try:
        time.sleep(1)
        temperature=arduino.readline()
        humidity=arduino.readline()
        print(data1)
        print(data2)

        try:
            #to insert a record
            mycursor = mydb.cursor()

            sql = "INSERT INTO dht11 (Humidity, Temperature) VALUES (%s, %s)"
            val = (humidity,temperature)
            mycursor.execute(sql, val)

            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
        except:
            print("Failed to insert data")
        finally:
            cursor.close()

    except:
        print("Failed to get data from arduino")
    
    a=a+1

    


    

#to delete a record
#mycursor = mydb.cursor()
#sql = "DELETE FROM dht11 WHERE Humidity=''"

#mycursor.execute(sql)

#mydb.commit()

#print(mycursor.rowcount, "record deleted.")
