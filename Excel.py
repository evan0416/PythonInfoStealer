import openpyxl

# 엑셀 파일을 선언
book = openpyxl.Workbook()

sheet = book.active
sheet.append([1,2,3,4,5])
sheet.append(["123"])