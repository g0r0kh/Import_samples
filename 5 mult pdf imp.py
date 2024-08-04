# pip install tabula-py
# sudo apt install openjdk-8-jdk # try to except err for Linux tabula.errors.JavaNotFoundError: `java` command is not found from this Python process.

import pandas as pd # call table module
import glob # call directory viewer
import tabula # call pdf viewer

pdf_files = glob.glob('*.pdf') # directory viewer for exac files

df = pd.DataFrame()
filename_col = pd.Series([],
                         dtype='str') # add file name column
for pdf_file in pdf_files:
    pdf_table = tabula.read_pdf(pdf_file,
                             pages='all',
                             multiple_tables=True,
                             lattice=True)

    for pdf_table in pdf_tables:
        if pdf_table.columns[0] == 'Цифр. код':
           df = pd.concat([df, pdf_table])

           filename = pd.Series([pdf_file]).repeat(len(pdf_table.index)) # add file name column
           filename_col = filename_col._append(filename) # add file name column
        else:
           continue
# necessary exec for series concat

df = df.reset_index(drop=True)
filename_col = filename_col.reset_index(drop=True)
df = pd.concat([df, filename_col.rename('file_name')],
               axis=1)



# df_single.to_csv('pdf_2_csv.csv',
#                   encodings='cp1251',
#                   sep=';')               # miss


df.to_csv('pdf_2_csv.csv', header = True, doublequote = False)