import pandas as pd
import matplotlib.pyplot as plt

def obesity(excelfile="Obes-phys-acti-diet-eng-2014-tab.xls", nogui = False):
    data = pd.ExcelFile(excelfile)
    print(data.sheet_names)

    # Read 2nd section, by age
    data_age  = data.parse('7.2', skiprows=4, skipfooter=14)

    # Rename unames to year
    data_age.rename(columns={'Unnamed: 0': 'Year'}, inplace=True)

    print(data_age)


if __name__ == "__main__":
    obesity()
