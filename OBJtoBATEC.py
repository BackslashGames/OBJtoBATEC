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
