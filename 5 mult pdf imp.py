# pip install tabula-py
# sudo apt install openjdk-8-jdk # try to except err for Linux tabula.errors.JavaNotFoundError: `java` command is not found from this Python process.

import pandas as pd # call table module
import glob # call directory viewer
import tabula # call pdf viewer

pdf_files = glob.glob('*.pdf') # directory viewer for exac files

df = pd.DataFrame()
for pdf_file in pdf_files:
    pdf_table = tabula.read_pdf(pdf_file,
                             pages='all',
                             multiple_tables=True,
                             lattice=True)

    for pdf_table in pdf_tables:
        if pdf_table.columns[0] == 'Цифр. код':
           df = pd.concat([df, pdf_table])
        else:
           continue


# df_single.to_csv('pdf_2_csv.csv',
#                   encodings='cp1251',
#                   sep=';')               # miss


df.to_csv('pdf_2_csv.csv', header = True, doublequote = False)