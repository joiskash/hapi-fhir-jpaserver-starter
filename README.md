# HAPI FHIR Server Setup

This repository contains code for setting up a HAPI FHIR server and loading synthetic patient data using Synthea.

## Required Python Libraries

Make sure the following Python libraries are installed on your system before running the data loading script:

- `glob`
- `os`
- `requests`

You can install these libraries using the following command:

```bash
pip install glob2 json5 os subprocess32 requests
```

Note: Make sure to replace glob2 with glob if you are using Python 3.5 and above.


## Setup Instructions

1. Navigate to the project directory:
   ```bash
   cd hapi-fhir-jpaserver-starter
 
2. Run the HAPI FHIR server using Docker Compose:  
   ```bash
   docker-compose up

3. Wait for the Synthea service to generate JSON files. The service will automatically stop after generating the files.
4. Once the service is stopped, run the Python script to upload the generated JSON files to the FHIR server:
   ```bash
   python3 fhir_data_loader.py
This script will handle the data loading process.

## Notes

- Ensure that Docker and Docker Compose are installed on your system.
- The Synthea service generates synthetic patient data in JSON format.
- The `fhir_data_loader.py` script uploads the generated JSON files to the HAPI FHIR server.
