import glob
import os
import requests

#fhir server endpoint
URL = "http://localhost:8080/fhir/"

#fhir server json header content
headers = {"Content-Type": "application/fhir+json;charset=utf-8"}
print("started running script")
def process_and_upload_file(file_path):
    with open(file_path, "r", encoding="utf8") as bundle_file:         
            data = bundle_file.read()
            r = requests.post(url = URL, data = data.encode("utf-8"), headers = headers)
            #output file name that was processed
            print(file_path)

script_directory = os.path.dirname(os.path.abspath(__file__))

# Assuming the output/fhir directory is inside the parent directory
relative_path = "output\\fhir"
# Construct the full path
full_path = os.path.join(script_directory, relative_path)

for dirpath, dirnames, files in os.walk(full_path):

    pattern = os.path.join(full_path, "hospitalInformation*.json")
    hospital_files = glob.glob(pattern)

    for file_path in hospital_files:
        process_and_upload_file(file_path)

    pattern = os.path.join(full_path, "practitionerInformation*.json")
    practitioner_files = glob.glob(pattern)

    for file_path in practitioner_files:
        process_and_upload_file(file_path)

    for file_name in files:
        file_path = os.path.join(full_path, file_name)
        process_and_upload_file(file_path)
    print("completed")  
        

