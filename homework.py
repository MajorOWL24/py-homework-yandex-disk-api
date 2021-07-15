import requests
import os

token = ""

class YaUploader:
  def __init__(self, file_path):
    self.file_path = file_path

  def upload(self):
    result = 0
    path = self.file_path
    filename = os.path.basename(path)

    url = "https://cloud-api.yandex.net/v1/disk/resources/upload?path=" + filename + "&overwrite=true"
    headers = {
      "Authorization": "OAuth AQAAAAAiALAKAADLW8Ec-ryjPEZspt4W-7NbNpg"
    }

    r = requests.get(url, headers=headers).json()
    if "href" in r:
      r = requests.put(r["href"], data=open(path, "rb").read(), headers=headers)
      if r.status_code == 201:
        result = 1

    # Тут ваша логика
    if result == 1:
      return "Файл " + filename + " успешно загружен"
    else:
      return "Не удалось загрузить файл " + path


if __name__ == '__main__':
    uploader = YaUploader('./test.txt')
    result = uploader.upload()
    print(result)
