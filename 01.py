import xlrd, csv, xlwt
from os import listdir
#init

def extract():

    global ws
    #      Назва клінічного випробування, код, версія та дата (здесь лучше отдельно также вытянуть код дослідження (в название страницы) и фаза, если есть)
    # ·         Заявник, країна (заявитель может повторяться в разных исследованиях)
    # ·         Спонсор, країна (спонсор может повторяться в разных исследованиях)
    # ·         Перелік досліджуваних лікарських засобів лікарська форма, дозування, виробник, країна
    # ·         Відповідальний (і) дослідник (и) та місце (я) проведення випробування в Україні (здесь, как правило, несколько центров. Желательно их разделить. Центры в разных исследованиях могут повторяться. Когда будешь разбивать этот параметр - исследователи тоже могут повторяться.) Лучше: місце проведення випробування; адреса; Відповідальний дослідник
    # ·         Препарати порівняння, виробник та країна
    # ·         Супутні матеріали/препарати супутньої терапії

    # out_file = open('2015.csv', 'w')
    # outcsv = csv.writer(out_file)
    # outcsv = csv.DictWriter(out_file,
    #                         fieldnames=['номер','Назва клінічного випробування',
    #                                     'Заявник', 'Спонсор',
    #                                     'Перелік досліджуваних засобів',
    #                                     'Відповідальний дослідник',
    #                                     'Препарати порівняння',
    #                                     'Супутні матеріали'])
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

                out_file.write(str(out_row))
                out_file.write(title)
    
                # print(out_row)
                # print(title)
                # print(zayavnyk)
                # print(sponsor)
                # print(tocompare)
                # print(bonus)

                # outcsv.writerow([out_row, title,
                #                  zayavnyk, sponsor,
                #                  drugslist, responder,
                #                  'tocompare', 'bonus'])

                # ws.write(out_row, 0, dgst_num)
                # ws.write(out_row, 1, title)
                # ws.write(out_row, 2, zayavnyk)
                # ws.write(out_row, 3, sponsor)
            row += 1
        print(out_row)
        out_file.close()


wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')
ws.write(0, 0, 'Test')
# try:
#     extract()
# except Exception as e:
#     print('some **it happens')
#     print(e)
extract()

wb.save('2015.xls')
