# MixedDateFormats
Convert date formats in a dataframe using python class.


Example:

t5 = MixedDateformats("C:/something/a***/Desktop/SLO_Data.csv")

# The format for the method is datefromatchange(x,old_date_format=...,New_date_format=...,New_var_name=...,final_filename=...)
t5.dateformatchange("DATE",'%m/%d/%Y','%m/%d/%Y',"Date1","gfinal.csv")
