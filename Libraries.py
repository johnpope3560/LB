import os
import requests
url = "https://raw.githubusercontent.com/pylist/pylist/main/py lists.py/Libraries.py"
if not os.path.exist("FetchedImages"):
    os.makedirs("FetchedImages")
    response = requests.get(url,stream=True)
    response.raise_for_status(5)
    filename = os.path.join("FetchedImages","image.jpg")
    for chunk in response.iter_content(chunk_size=8192):
        file.write(chunk)
        print(f"Image successfully downloaded:{filename}")
print (f"An error occurred:.The connection may have failed.")