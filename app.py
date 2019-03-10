
import cv2
import numpy as np
import pytesseract
import mysql.connector
import os


def Create_Record_File(file_path,file_text):
    print("Creating File...")
    try:
     file= open(file_path,'w')
     file.write(file_text)
     file.close()
    except IOError:
        print("File not found or path is incorrect")
    finally:
        print("done Create_Record_File Function")


def Delete_Db_Record(db_cursor,id_table,my_db):
    print("Removing record...")
    try:
       sql = "DELETE FROM recordfile WHERE filename = %s"
       id_table = (id_table,)
       db_cursor.execute(sql,id_table)
       my_db.commit()
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    finally:
        print("Done Delete_Db_Record Function")




mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "123456"
)

#print(mydb)
mycursor = mydb.cursor()
mycursor.execute("use sys")

mycursor.execute("SELECT * FROM recordfile ")

list_path = [x for x in mycursor]






for file_name, path in list_path:
   # file_name, path = list_path[0]

    img = cv2.imread(str(path+file_name))
   # cv2.imshow('img', img)
    grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    img_string = pytesseract.image_to_string(th,lang='por')

    print(path+file_name)
    Create_Record_File(file_path=  'D:\\Programacao\\data\\text-pic\\'+file_name.split('.')[0]+'.txt',file_text=img_string)
    if (os.path.exists(path+file_name) ):
       print("Removing pic file ")
       os.remove(path+file_name)
    Delete_Db_Record(mycursor,file_name,mydb)



# print(img_string)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("process is done")
mydb.close()
