##-----------------IMPORTING PANDAS LIBRARY--------------------------
import pandas as pd

##-----------------INITIALIZING .csv FILE----------------------------
csv_ctx = pd.read_csv("D:/ip-project-file/bank_data.csv",)

##------------------PERFORMING OPERATIONS----------------------------

print("Shape : ",csv_ctx.shape)

print("First n Elements : ",csv_ctx.head(1))

print("Last n Elements : ",csv_ctx.tail(1))

print("Size : ",csv_ctx.size)

print("DataType : ",csv_ctx.dtypes)

print("Columns : ",csv_ctx.columns)

print("All Elements : ",csv_ctx.values)
