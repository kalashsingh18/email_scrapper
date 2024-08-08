import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time 
import pandas as pd
import send_email
from datetime import datetime, timedelta

# Define the scope
def extract_data_():
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
# Path to your credentials JSON file
    creds_path = 'service_account.json'

    try:
        creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
        client = gspread.authorize(creds)
        sheet_name = "chatgpt_check sheet"
        sheet = client.open(sheet_name)
        global worksheet
        worksheet=sheet.worksheet('Ips Hackathon Responses')
        data=worksheet.get_all_values()# Open the first sheet
        # records = sheet.get_all_records()
        # print(records) 
           
        return data[0:]
    except Exception as e:
        print(f"An error occurred: {e}")

global_participants_list=[]
print(global_participants_list)
def check_and_notify(data):
    EMAIL_SENT_COL_IDX=2
    for row in data:
        unique_participants=check_for_duplicate_participants(row)
        for participant_key in unique_participants:
            global_participants_list.append(participant_key)

        if row[-1]!="Yes" and len(unique_participants) > 0:
            team_name=row[1]
            counter=0
            for _,_,email in unique_participants:
                send_email.send(email,team_name)

            counter+=1
            worksheet.update_cell(EMAIL_SENT_COL_IDX, 21, "Yes") 

        EMAIL_SENT_COL_IDX+=1

def check_for_duplicate_participants_helper(unique_participants, participant_key):
    return (participant_key not in global_participants_list \
        and participant_key not in unique_participants \
        and participant_key[1] not in [phone for _,phone,_ in unique_participants] \
        and participant_key[2] not in [email for _,_,email in unique_participants] \
        and participant_key[1] not in [phone for _,phone,_ in global_participants_list] \
        and participant_key[2] not in [email for _,_,email in global_participants_list])

def check_for_duplicate_participants(row):
    unique_participants=[]
    for participant_key in filter_data(row):
        if check_for_duplicate_participants_helper(unique_participants, participant_key):
            unique_participants.append(participant_key)  
        else: 
            break              
    else: 
        return unique_participants 
    return []
                 
def filter_data(data):
    PARTICIPANT_1_UNIQUE_KEYS = (2,3,4)
    PARTICIPANT_2_UNIQUE_KEYS = (6,7,8)
    PARTICIPANT_3_UNIQUE_KEYS = (10,11,12)

    PARTICIPANT_KEYS_LIST = []
    for name_col_idx, email_col_idx, phone_col_idx in \
    [PARTICIPANT_1_UNIQUE_KEYS, PARTICIPANT_2_UNIQUE_KEYS, PARTICIPANT_3_UNIQUE_KEYS]:
        PARTICIPANT_KEYS_LIST.append((data[name_col_idx], data[phone_col_idx], data[email_col_idx]))

    return PARTICIPANT_KEYS_LIST

def drop_duplicates(data):
     df = pd.DataFrame(data[1:], columns=data[0]) 
     return df.values.tolist() 
                
if __name__=="__main__":
    data=extract_data_()
    print(data)
    data=drop_duplicates(data)
    
    check_and_notify(data)
    
                 
                       
                       
                        
                  
                  
                    
                     
                      
 
    
                  
           

        

            # Check if registration time is within the current time window




    





   

    
   


    
    
   
    

    
    
   
    

    
   

    
