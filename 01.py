import xlrd, csv, xlwt
from os import listdir
#init

def extract():
    out_file=open('2015.txt','w')
    out_row = 0
    for file in listdir('./2015'):
        dgst_num = file[13:16]
        # 'dn_20150522_0300_dod1-14.xls'
        rb = xlrd.open_workbook('2015/' + file)
        sheet = rb.sheet_by_index(0)
        print(sheet.nrows)
        row = 0
        while row < sheet.nrows:
            current = sheet.cell(row, 0).value
            if current == 'Затвердження клінічного випробування':
                out_row += 1
                title = repr(sheet.cell(row + 2, 1).value)
                zayavnyk = repr(sheet.cell(row + 3, 1).value.strip('"'))
                sponsor = repr(sheet.cell(row + 4, 1).value)
                drugslist = sheet.cell(row + 5, 1).value
                responder = sheet.cell(row + 6, 1).value
                tocompare = sheet.cell(row + 9, 1).value
                bonus = sheet.cell(row + 10, 1).value
                print(out_row, title[:25], zayavnyk[:25], drugslist[:25])

                out_file.write(str(out_row)+"\n")
                out_file.write(title+'\n')
                out_file.write(zayavnyk+'\n')
                out_file.write(sponsor+'\n')
                out_file.write(drugslist+'\n')
                out_file.write(responder+'\n')
                out_file.write(tocompare+'\n')
                out_file.write(bonus+'\n')

            row += 1
        print(out_row)
    out_file.close()


extract()

