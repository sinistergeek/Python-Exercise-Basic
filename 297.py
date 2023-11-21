import zipfile

path = "developer_survery_2019.zip"
z = zipfile.ZipFile(path)
z.extractall()
