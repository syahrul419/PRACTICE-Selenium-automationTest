from xlrd import open_workbook

'''
data with excel file - used
'''
class dataReader:
    @staticmethod
    def readDataForLogin():
        book = open_workbook('data.xlsx')
        first_sheet = book.sheet_by_index(0)
        data = []
        for i in range(1, first_sheet.nrows):
            email = first_sheet.cell_value(i, 0)
            expected = first_sheet.cell_value(i, 1)
            dataTuple = (email, expected)
            data.append(dataTuple)
            dataTuple = ()
        return data

if __name__ == "__main__":
    dataReader.readDataForLogin()


'''
data with json file - not used
'''
# class dataReader:
#     @staticmethod
#     def readDataForLogin():
#         f = open("data.json")
#         data = json.load(f)
#         dataPwd = data["pwd"]
#         dataEmail = []
#         for i in data["email"]:
#             dataEmail.append(i)
#         return dataEmail, dataPwd
        
# if __name__ =="__main__":
#     dataReader