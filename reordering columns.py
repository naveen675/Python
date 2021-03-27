import pandas as pd
import sys
import openpyxl

 
import os
 
if __name__ == "__main__":
    
    directory ="C:\Development avecto\Column_reordering"     #input file directory
    dc = "C:\Development avecto\csv files"      #Output file directory
    
    dic = dict()
 
    #Config file where structured column names along with file name 
    # will be placed in comma delimited

    with open("config.txt") as fp:     
        lines = fp.readlines()
 
        for line in lines:
 
            columns = line.strip().split(",")
            name = columns[0]
            columns = columns[1:]
            if(name):
                dic[name] = columns
 
    # print(dic)
 
    files = os.listdir(directory)          
 
 #Iterating each unstructured excel file in directory

    for file in files:                          
        
        extension = ""
        count=0
        #print(file)
        file_name, extension = file.split(".")

        generic_name=""
        date=""
        li = file_name.split("_")
        generic_name=li[0]
 
        if(extension!='xlsx'):                  #checking for Excel file
            print(file_name)
            continue
 
        path = os.path.join(directory, file)
        # print(path)
 
 
        if(dic.__contains__(generic_name)):           #checking for the excel file exist in config file

            print("{} present".format(file))

            book = openpyxl.load_workbook(path)
            sheet = book.active

    # To remove unwanted rows or cells in excel

            for rows in sheet:
                status = False
                for col in rows:
                    if col.value==None:    
                        count = count+1
                        status = True
                        break
                if status == False:
                    break   
            

            read_file = pd.read_excel(path,skiprows = count)
            
            read_fle
            print("Before rearranging the columns....\n")
            #print(pd.DataFrame(read_file))
            print()
            df = pd.DataFrame(read_file, columns = dic[generic_name] )
            #print(read_file)
            df.rename({"RSU":"ASIN"}, axis='columns')
            print("After rearranging the columns....\n")
            df['filename'] = file

            #print(df)
            writer = pd.ExcelWriter(file)
            df.to_excel(writer,index=False )
            writer.save()
            read_file = pd.read_excel(path)
            
            file_path = "{}/{}.csv".format(dc, file_name)

            #structured data writing into csv file 
            
            read_file.to_csv(file_path, index=None, header=True, columns=dic[generic_name])
        else:
            print("File name not present in config file") 
