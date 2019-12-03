# class FilterModule(object):
#     def dict_to_excel(self,col,data,save_fn,newline=True):
#     # get data to enter to exisiting excel file and insert it in the next free raw
#     # col - column to insert the data too 
#     # data - data to insert to excel 
#     # save_fn - file to be saved 
#     # newline - to insert the data in a new line or in the last line 
#     wb=load_workbook(filename=save_fn)
#     sheet=wb.active
#     if newline == True:
#         sheet. cell(sheet.max_row+1,col,data)
#     else:
#           sheet.cell(sheet.max_row,col,data)  
#     wb.save(filename=save_fn)
       

#     def filters(self):
#         return {
#             'dict_to_excel': self.dicsort
#         }