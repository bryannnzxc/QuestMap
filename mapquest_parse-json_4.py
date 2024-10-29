import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "fZadaFOY22VIEEemZcBFfxl5vjSXIPpZ" #Replace with your MapQuest key

while True:
   orig = input("Starting Location: ")
   if orig == "quit" or orig == "q":
        break
   dest = input("Destination: ")
   if dest == "quit" or dest == "q":
        break

json_data = requests.get(url).json()
print(json_data)
print("URL: " + (url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
            print("API Status: " + str(json_status) + " = A successful route call.\n")