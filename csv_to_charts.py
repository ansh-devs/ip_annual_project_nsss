##------IMPORTING LIBRARIES--------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

##------INITIALIZING .csv FILE-----------------------------------------
csv_ctx = pd.read_csv("D:/ip-project-file/bank_data.csv")

##------EXTRACTING COLUMNS AS ARRAYS-----------------------------------
x_axis=csv_ctx['NAME']
y_axis=list(csv_ctx['SAVINGS IN $'])
credited_axis=list(csv_ctx['MAXIMUM_CREDITED'])
debited_axis=list(csv_ctx['MAXIMUM_DEBITED'])


##------PLOTTING BAR CHART---------------------------------------------
plt.bar(x=x_axis,data=y_axis,height=y_axis,color = "#6C00FF",edgecolor="#FF8E9E")
plt.xlabel('Savings in Dollars $')
plt.ylabel('Account Owner Names')
plt.title('Bar Chart Representation Of Bank Data')
plt.show()


##------PLOTTING HORIZONTAL BAR CHART----------------------------------
plt.barh(data=x_axis,width=y_axis,color = "#6C00FF",edgecolor="#FF8E9E",y=x_axis)
plt.xlabel('Savings in Dollars $')
plt.ylabel('Account Owner Names')
plt.title('Horizontal Bar Chart Representation Of Bank Data')
plt.show()

##------PLOTTING SCATTER CHART-----------------------------------------
plt.scatter(color = "#6C00FF",edgecolor="#FF8E9E",y=credited_axis,x=x_axis)
plt.xlabel('Savings in Dollars $')
plt.ylabel('Account Owner Names')
plt.title('Scatter Chart Representation Of Bank Data')
plt.show()

##------PLOTTING LINE CHART--------------------------------------------
plt.plot(x_axis,debited_axis,'--',linewidth=2.5,color='red',marker='o',markerfacecolor='yellow',markersize=5)
plt.xlabel('Account Owner Names')
plt.ylabel('Max. amount debited last month')
plt.title('Line Chart Representation Of Bank Data')
plt.show()

##------PLOTTING Dual-Bar CHART----------------------------------------
new_x_axis=np.arange(len(list(x_axis)))
plt.bar(new_x_axis - 0.2,y_axis,0.4,label='SAVINGS')
plt.bar(new_x_axis + 0.2,credited_axis,0.4,label='CREDITED')
plt.xticks(new_x_axis,x_axis)
plt.xlabel('Account Owner Names')
plt.legend()
plt.title('Dual-Bar Chart Representation Of Bank Data')
plt.show()