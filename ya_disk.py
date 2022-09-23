
import requests
import os.path


class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def upload_file_to_disk(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        hh = os.path.normpath(disk_file_path)
        filename = os.path.split(hh)[-1]
        params = {"path": f"/Загрузки/{filename}", "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params).json()
        href = response.get("href", "")
        response = requests.put(href, data=open(disk_file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")
