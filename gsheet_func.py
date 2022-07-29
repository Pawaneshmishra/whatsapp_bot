import gspread
from oauth2client.service_account import ServiceAccountCredentials

s=['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', s)
client = gspread.authorize(creds)

sheet = client.open("remainder").sheet1
row_values = sheet.row_values(1)
col_values = sheet.col_values(1)
row_filled = len(row_values)
col_filled = len(col_values)

def save_remainder_date(date):
    sheet.update_cell(row_filled+1, 1, date)
    print("Date saved!")
    return 0

def save_remainder_body(body):
    sheet.update_cell(row_filled+1, 2, body)
    print("Body saved!")
    return 0    