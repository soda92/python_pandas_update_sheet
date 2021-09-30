import pandas as pd
from pathlib import Path
CURR_DIR = Path(__file__).resolve().parent

file1 = Path.joinpath(CURR_DIR, "data1.xlsx")
file2 = Path.joinpath(CURR_DIR, "data2.xlsx")

df1: pd.DataFrame = pd.read_excel(file1, sheet_name='明细')
df2: pd.DataFrame = pd.read_excel(file2, sheet_name='明细2')

with pd.ExcelWriter(file1, engine='openpyxl', mode='a') as writer:
    df2.to_excel(writer, sheet_name="明细2")
