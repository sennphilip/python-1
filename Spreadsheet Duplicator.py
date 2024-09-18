import gspread
from google.oauth2.service_account import Credentials
#from oauth2client.service_account import ServiceAccountCredentials

scopes = ['https://spreadsheets.google.com/feeds',
          'https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']

cred1 = Credentials.from_service_account_file('sheets-key.json', scopes=scopes)#MyCSQKey rep by M
#cred = ServiceAccountCredentials.from_json_keyfile_name('sheets-key.json', scopes=scope)


client1 = gspread.authorize(cred1)

spreadsheet1 = client1.open("TowerCo Analysis")
spreadsheet2 = client1.open("TOWERS - ALL")


A = spreadsheet1.worksheets()

#Title = [i.title for i in A]
Title = map(lambda i: i.title, A)

print(Title)
#print('--------------------------------')
#print(spreadsheet2.worksheets())
for x in Title:
    if x in spreadsheet2:
        x = x + '*'

    sheet1 = spreadsheet1.worksheet(x)
    spreadsheet2.add_worksheet(title=sheet1.title, rows=sheet1.row_count, cols=sheet1.col_count)
    sheet2 = spreadsheet2.worksheet(sheet1.title)
    cell_range = sheet1.get_all_values()
    sheet2.update('A1', cell_range)
