import csv

def csv_to_list(csvfile):
    with open(csvfile, encoding = 'Big5') as f:
        fieldnames = ['日期', '開盤指數', '最高指數', '最低指數', '收盤指數']
        reader = csv.DictReader(f, fieldnames = fieldnames)
        return list(reader)[2:-2]

def row_with_fields(row, fieldnames):
    return {fieldname : row[fieldname] for fieldname in fieldnames}

def index_with_fields(index_data, fieldnames):
    return (row_with_fields(origin_row, fieldnames) for origin_row in index_data)

csvfile = input('CSV檔案名稱：')
fieldnames = input('查詢欄位：').split(",")
index_data = csv_to_list(csvfile)

for name in fieldnames:
    print(name, end = '\t\t')
print()

for row in index_with_fields(index_data, fieldnames):
    for name in fieldnames:
        print(row[name], end = '\t\t')
    print()
