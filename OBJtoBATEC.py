#ObjToBatec for HyperFlux by ImFromTheOtherOS (or OtherOS)
#Hello, World!
#_#

#-----------#
#Changelog- ver:1.0b
#initial release, converts "v:" part of .obj text to BATEC.
#-----------#

# opens some files, the input, lengthID and a new output file.
file = (open("input.txt","r"))
out = (open("output.txt","w+"))
lengthid = (open("LengthID.txt","w+"))
# makes variables
cv = "place holder"
end = ""
count = int("0")
#cv stands for convert, this bit does the things!
while cv != " ":
    cv = file.read(12)
    count = int(count)
    count += 1
    count = str(count)
    lengthid.write(count)
    lengthid.write("\n")
    print(cv)
    cv = float(cv)
    cv = int(cv)
    print(cv)
    cv = cv + 10000
    cv = str(cv)
    out.write(cv)
# while loop doesnt technically end, it intentionally crashes
