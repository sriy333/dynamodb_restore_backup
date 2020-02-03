import json
import os
import time
from . import constants

class JsonFormatter:

    def insert_credentials_via_cli(self):
        os.system('start cmd.exe')
        os.system("aws configure")
        os.system(constants.AWS_KEY_ID)
        os.system(constants.AWS_KEY_SECERT_ID)

    def fetching_data_from_dynamodb(self):
        os.system('start cmd.exe')
        os.chdir("C:\\Users\\z003u7pv\\PycharmProjects\\dynamodbBackup\\test")
        records = os.system('aws dynamodb scan --table-name Credentials > export.json')
        records = json.loads(open("C:/Users/z003u7pv/PycharmProjects/dynamodbBackup/test/export.json").read())
        records_count = records["Count"]
        print("Total records were found :" +records_count)
        os.system('aws dynamodb scan --table-name Credentials --query Items[] > export.json')
        print("successfully loaded data and Intial phase of backing up data is completed")

    def fetching_from_file(file_path):
        json_data = json.loads(open(file_path).read())
        json_index_list = list(range(0, len(json_data), 25))
        if json_index_list[-1] == len(json_data):
            batch_index_list = list(zip(json_index_list[-1:], json_index_list))
        else:
            json_index_list.append(len(json_data))
            batch_index_list = list(zip(json_index_list[1:], json_index_list))
        if batch_index_list is not None:
            for i in batch_index_list:
                with open('input.json', 'w') as the_file:
                    json.dump(json_data[i[1]:i[0]], the_file, indent=4, sort_keys=True)
                    tablename = {}
                    tablename[str(constants.TABLE_NAME)] = []
                    backup_test = tablename[str(constants.TABLE_NAME)]
                    for it in json_data[i[1]:i[0]]:
                        data = {"PutRequest": {"Item": it}}
                        backup_test.append(data)
                with open('input1.json', 'w') as the_file1:
                    the_file1.write(json.dumps(tablename, indent=4, sort_keys=True))
                    os.system('start cmd.exe')
                    os.chdir("C:\\Users\\z003u7pv\\PycharmProjects\\dynamodbBackup\\test")
                    os.system('aws dynamodb batch-write-item --request-items file://input1.json')
                    time.sleep(5)
            print("successfull")
