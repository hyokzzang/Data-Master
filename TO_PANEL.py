# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 11:59:05 2014

@author: HJK

Program for seasonal adjustment using X-12 ARIMA

"""

import pandas as pd

MAIN_PATH = "C:/Users/KIET/Desktop/NEW_FTA_PROJ"
REER_PATH = "/REER/WORLD_BANK_REER.xlsx"
GDP_PATH = "/GDP_WORLDBANK/WORLD_BANK_GDP2.xlsx"

DATA_REER = pd.io.excel.read_excel(MAIN_PATH+REER_PATH, sheetname = 0, skiprows = 0, index_col = 0, header = 0)

STACKED_REER = DATA_REER.stack()

STACKED_REER.to_csv("STACKED_REER.csv")

DATA_GDP = pd.io.excel.read_excel(MAIN_PATH+GDP_PATH, sheetname = 0, skiprows = 0, index_col = 0, header = 0)

STACKED_GDP = DATA_GDP.stack()

STACKED_GDP.to_csv("STACKED_GDP.csv")