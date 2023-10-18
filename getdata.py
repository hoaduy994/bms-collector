import requests
import xml.etree.ElementTree as ET
import time
from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("HOST")
TM_URL = os.getenv("TM_URL")
CT_URL = os.getenv("CT_URL")
PORT = os.getenv("PORT")

api_urls = {
    "cua_tu": f"http://{HOST}:{PORT}/{CT_URL}",
    "thang_may": f"http://{HOST}:{PORT}/{TM_URL}",
}
print(HOST)
print(TM_URL)
print(CT_URL)
print(PORT)
print(api_urls)

output_dir = "/app/output"  

while True:
    for api_name, api_url in api_urls.items():
        try:
            response = requests.get(api_url)
            response.raise_for_status()

            filename = api_name + ".xml"
            filepath = os.path.join(output_dir, filename)
            with open(filepath, "w") as file:
                file.write(response.text)

            print(f"Lưu file {filename} thành công")

        except requests.exceptions.RequestException as e:
            print(f"Lỗi khi gửi yêu cầu GET đến {api_name}: {e}")

    time.sleep(5)