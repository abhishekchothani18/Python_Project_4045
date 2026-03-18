import zipfile


zip_to_extract = "my_archive.zip"

with zipfile.ZipFile(zip_to_extract, 'r') as my_zip:

    my_zip.extractall("extracted_files")
    print("Files have been unzipped!")