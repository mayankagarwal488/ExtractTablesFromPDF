import pandas as pd
import tabula
from tabula import read_pdf

df=read_pdf("table.pdf")
print (df)


