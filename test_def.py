def in_Excel(file_path):
    data_file = pd.read_excel(file_path)
    dataF = data_file.ix[:, :]
    data_matrix = np.matrix(dataF)
    return(data_file, dataF, data_matrix)
    
def isNaN(num): #判断是不是Nan
    return num != num

