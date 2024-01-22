import json
import os
import subprocess
import time
import requests

#fhir server endpoint
URL = "http://hapi-fhir-jpaserver-start:8080/fhir/"

#fhir server json header content
headers = {"Content-Type": "application/fhir+json;charset=utf-8"}

def process_and_upload_file(file_path):
    with open(file_path, "r", encoding="utf8") as bundle_file:         
            data = bundle_file.read()
            r = requests.post(url = URL, data = data.encode("utf-8"), headers = headers)
            #output file name that was processed
            print(file_path)

#loop over all files in the output folder in order to upload each json file for each patient.
for dirpath, dirnames, files in os.walk("/usr/app/src/fhir"):
    print("started")
    process_and_upload_file("/usr/app/src/fhir/hospitalInformation1705300016107.json")
    process_and_upload_file("/usr/app/src/fhir/practitionerInformation1705300016107.json")
    for file_name in files:
        process_and_upload_file("/usr/app/src/fhir/"+file_name)
    print("completed")        

