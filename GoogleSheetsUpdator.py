'''
Created on 19-Aug-2018
Class for updating Google spreadsheet
Code from https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
@author: sethu
'''

import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GoogleSheetsUpdator():
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('google_drive_client_id.json', scope)
    client = gspread.authorize(creds)
    
    row_index = 2;
       
    def insertRow(self, row):
        #Find a workbook by name and open the first sheet. Make sure to use the right name
        sheet = GoogleSheetsUpdator.client.open("temp_sheet").sheet1
        sheet.insert_row(row, GoogleSheetsUpdator.row_index)
        GoogleSheetsUpdator.row_index += 1
    
    def readRecords(self):
        sheet = GoogleSheetsUpdator.client.open("temp_sheet").sheet1
        
        # Extract and print all of the values
        all_records = sheet.get_all_values()
        print(all_records)
        
if __name__ == '__main__':
    obj = GoogleSheetsUpdator()
    obj.readRecords()
    obj.insertRow(["I'm","inserting","a","row","into","a,","Spreadsheet","with","Python"])
    obj.readRecords()
    
    
    
    
