import zipfile


zip_name = "my_archive.zip"


files_to_zip = ["readme.txt", "notes.txt"]

with zipfile.ZipFile(zip_name, 'w') as my_zip:
    for file in files_to_zip:
        my_zip.write(file)
        print(f"Added {file} to the zip.")

print("Success! Your zip file is ready.")