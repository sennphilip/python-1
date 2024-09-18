import gspread
from google.oauth2.service_account import Credentials
#from oauth2client.service_account import ServiceAccountCredentials

scopes = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

credM = Credentials.from_service_account_file('sheets-key.json', scopes=scopes)#MyCSQKey rep by M
credC = Credentials.from_service_account_file('csqsheetsapi.json', scopes=scopes)#MyCSQKey rep by C
#cred = ServiceAccountCredentials.from_json_keyfile_name('sheets-key.json', scopes=scope)


clientM = gspread.authorize(credM)
clientC = gspread.authorize(credC)

#sheetM = '1MoTXDsRrPkLI_vGtcaKd0NLNEBp7Z8Rt_mw7AsUzmWA'#python_sheet
#sheetC = '1XNwe-ppGefh8jfhnml3LkZv7zgg0GroLMP-E5iJd9Rk'#[Master] Site Installation Costing (2024)
#sheetM = "1vpzYJ9yA3BIgtRX8rzzkLrhx7ajt2MaAZIFuQgheOgs"#LORDAKUFEX LIMITED
#sheetC = '11MgnM7T_vAITS9Sm4FwDGL-ZN2priW-POqwnl-ZUx8o'#Master Site Rollout Tracker - ver.5

#spreadsheetM = clientM.open_by_key(sheetM)
#spreadsheetC = clientC.open_by_key(sheetC)
#spreadsheet = client.open_by_url ("https://docs.google.com/spreadsheets/d/1MoTXDsRrPkLI_vGtcaKd0NLNEBp7Z8Rt_mw7AsUzmWA/edit#gid=0")
#spreadsheetA = clientM.open("Values")
#spreadsheetB = clientC.open("AERIAL")

spreadsheetM = clientM.open("TowerCo Analysis")
spreadsheetC = clientC.open("TOWERS - ALL")


print(spreadsheetM.worksheets())
#print('--------------------------------')
print(spreadsheetC.worksheets())


##Get the values on row 2
row_values = spreadsheetM.sheet1.row_values(2)
#row_values = spreadsheetM.worksheet('Test').row_values(3)
print(row_values)
#printing all worksheets in spreadsheet
# worksheets = map(lambda x: x.title, spreadsheet.worksheets())
worksheets = spreadsheetM.worksheets()
print(worksheets)
#selecting a worksheet to change the sheet name
worksheet1 = spreadsheetM.worksheet('Sheet1')
worksheet1.update_title("Test")
#selecting the worksheet to updated or format (cell values)
sheetTest = spreadsheetM.worksheet('Test')
sheetTest.format('A1', {"textFormat": {"bold": True}})
sheetTest.update_cell(1, 1, "Number")#To update a cell
sheetTest.update_acell('A1', "Numbers")#same as above
#print value in a cell & finding which cell value belongs to
cell_value = sheetTest.acell('A1').value
cell_find = sheetTest.find('Juliana Opokua Quaye')
print(cell_find.row, cell_find.col)

#creating a new worksheet
Newsheet = spreadsheetM.add_worksheet(title="Newsheet", rows=100, cols=20)
#Iterate over the list of names to create new worksheet for each
employee_names = ['Philip', 'Mosafo', 'Reggi', 'Jasper', 'Nana']
for name in employee_names:
 spreadsheetM.add_worksheet(title=name, rows=20, cols=20)

#deleting a worksheet
#spreadsheet.del_worksheet_by_id('170848470')
#deleting multiple worksheets (make sure they do not have protection)
worksheets = spreadsheetM.worksheets()
print(worksheets)
delete = ['559270747', '738555661', '840837357', '459622160', '314186471']
for i in delete:
   spreadsheetM.del_worksheet_by_id(i)

#duplicating a worksheet
spreadsheetM.duplicate_sheet(source_sheet_id=1480963219, insert_sheet_index=None, new_sheet_id=2, new_sheet_name='Try')
#spreadsheet.worksheet('Try').copy_to(sheetID)#used to create a copy without renaming

#Checking if sheet exist and populating it with values
values = [['Name', 'Price', 'Quantity'], ['Basketball', 29.9, 1], ['Jeans', 39.9, 2], ['Soap', 7.9, 3]]
worksheets = map(lambda x: x.title, spreadsheetM.worksheets())
newworksheet = "SheetA"
if newworksheet in worksheets:
   sheet = spreadsheetM.worksheet(newworksheet)
else:
   sheet = spreadsheetM.add_worksheet(newworksheet, rows=10, cols=10)
sheet.clear()#deleting values in the sheet if some values in the sheet already
sheet.update(f'A1:C{len(values)}', values)
#for i, row in enumerate(values):
   #for j, value in enumerate(row):
       #sheet.update_cell(i + 1, j + 1, value)
