# pip install tabula-py
# sudo apt install openjdk-8-jdk # try to except err for Linux tabula.errors.JavaNotFoundError: `java` command is not found from this Python process.

import pandas as pd # call table module
import glob # call directory viewer
import tabula # call pdf viewer

pdf_files = glob.glob('*.pdf') # directory viewer for exac files

pdf_tables = tabula.read_pdf(pdf_files[0],
                             pages='all',
                             multiple_tables=True)

# print(pdf_tables[0].columns[0]) # check 1st row

df_single = pd.DataFrame()
for table in pdf_tables:
    if table.columns[0] == 'Цифр. код':
        df_single = pd.concat([df_single, table])
    else:
        continue


# df_single.to_csv('pdf_2_csv.csv',
#                   encodings='cp1251',
#                   sep=';')               # miss


df_single.to_csv('pdf_2_csv.csv', header = True, doublequote = False)