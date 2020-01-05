import re

# data of date
with open("date.txt", "r", encoding="utf-8") as date_txt:
    date = date_txt.readlines()
DATE = date

# date :sample of Regular expression operations
date_type = re.compile(r"""(
    (^\d{4})        # First 4 digits number
    (\D)            # Something other than numbers
    (\d{1,2})       # 1 or 2 digits number
    (\D)            # Something other than numbers
    (\d{1,2})       # 1 or 2 digits number
    )""",re.VERBOSE)


for date in DATE:
    # Hit data to "hit_date"
    hit_date = date_type.search(date)
    bool_value = bool(hit_date)
    if bool_value is True:
        split = hit_date.groups()
        # Tuple unpacking
        year, month, day = int(split[1]),int(split[3]),int(split[5])

        if year>3000 or month >12 or day > 31:
            continue
        else:
            print(year, month, day)

    # if bool_value is True:
    #     stringed = hit_date.string
    #     #ここでは数字以外を"/"に変える
    #     r = re.sub(r"\D", "/",stringed,count=3)
    #     s = r.split("/")
    #     year = int(s[0])
    # else:
    #     print("False")
    #

