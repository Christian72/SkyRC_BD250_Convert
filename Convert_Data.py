import sys

# get filename
print ('argument list', sys.argv)
filename = sys.argv[1]

print ("Open {}. Converting to csv format.".format(filename))

# open and read line by line 
with open (filename) as fileread:
    lines = fileread.read().splitlines()

# open file to write
filewrite = open(filename+".csv", "w")

# print header information
print ("Time;Current;Voltage;Power;Capacity\n")
filewrite.writelines ("Time;Current;Voltage;Power;Capacity\n")

#concat 1st line of data
count = 0
print(lines[count] + ";" + lines[count+1] + ";" + lines[count+2] + ";" + lines[count+3] + ";" + lines[count+4] )
filewrite.writelines(lines[count] + ";" + lines[count+1] + ";" + lines[count+2] + ";" + lines[count+3] + ";" + lines[count+4] + "\n" )
count +=5
even = 1

#concat all lines, as time information are doubled up special handling (time info, time info + 0.5)
while count < len(lines):
    if even:
        print(lines[count] + ";" + lines[count+1] + ";" + lines[count+2] + ";" + lines[count+3] + ";" + lines[count+4] )
        filewrite.writelines(lines[count] + ";" + lines[count+1] + ";" + lines[count+2] + ";" + lines[count+3] + ";" + lines[count+4] + "\n" )
        even = 0
    else:
        print(lines[count] + ",5" + ";" + lines[count+1] + ";" + lines[count+2] + ";" + lines[count+3] + ";" + lines[count+4] )
        filewrite.writelines(lines[count] + ",5" + ";" + lines[count+1] + ";" + lines[count+2] + ";" + lines[count+3] + ";" + lines[count+4] +"\n" )
        even = 1

    count += 5


# close all files
fileread.close()
filewrite.close()