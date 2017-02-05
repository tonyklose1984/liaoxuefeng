#coding:utf-8
import xlsxwriter

work = xlsxwriter.Workbook('1.xlsx')

chart = work.add_chart()

worksheet = work.add_worksheet("tony")

worksheet.set_column("A:A",20)


bold = work.add_format({"bold":True})

worksheet.write('A1',"tony",bold)

work.close()