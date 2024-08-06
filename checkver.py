import json
import requests
import os
import zipfile

def run():
    r = requests.get("https://lewisdavies.me/nihongo/current_request.json")
    latest_ver = r.json()["current_version"]
    current_ver = json.load(open("data/package.json"))["version"]

    if current_ver != latest_ver:
        os.system("cls || clear")
        print("Update Available!")
        print(f"Current Version: {current_ver}")
        print(f"Latest Version: {latest_ver}")
        
        print(f"Beginning Update...")
        
        # Check temp folder exists
        if not os.path.exists("temp"):
            os.makedirs("temp")
        
        URL = "https://lewisdavies.me/nihongo/latest.zip"
        SAVE_PATH = "temp/latest.zip"

        def download_large_file(url, destination):
            try:
                with requests.get(url, stream=True) as response:
                    response.raise_for_status()
                    with open(destination, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            f.write(chunk)
                print("File downloaded successfully!")
                
                with zipfile.ZipFile("temp/latest.zip", 'r') as zip_ref:
                    zip_ref.extractall("temp/")
                
                os.remove("temp/latest.zip")
            except requests.exceptions.RequestException as e:
                print("Error downloading the file:", e)

        # Example usage
        download_large_file(URL, SAVE_PATH)
        os.system("cls || clear")