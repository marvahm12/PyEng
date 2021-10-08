import pandas as pd
import matplotlib.pyplot as plt

def obesity(excelfile="Obes-phys-acti-diet-eng-2014-tab.xls", nogui = False):
    data = pd.ExcelFile(excelfile)
    print(data.sheet_names)

    # Read section 7.1 from the Excel file

    # Define the columns to be read
    columns1 = ['year', 'total', 'males', 'females']
    #print(columns1)

    data_gender = data.parse(u'7.1', skiprows=4, skipfooter=14, names=columns1) 
    print (data_gender)
    print('hello')
    
    
if __name__ == "__main__":
    obesity()
