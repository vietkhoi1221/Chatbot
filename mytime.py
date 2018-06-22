import time
localtime = time.asctime( time.localtime(time.time()))
thu = ""
month_vn = ""
if localtime[0:3] == "Mon":
    thu = "Thứ 2,"
elif localtime[0:3] == "Tue":
    thu = "Thứ 3,"
elif localtime[0:3] == "Wed":
    thu = "Thứ 4,"
elif localtime[0:3] == "Thu":
    thu = "Thứ 5,"
elif localtime[0:3] == "Fri":
    thu = "Thứ 6,"
elif localtime[0:3] == "Sat":
    thu = "Thứ 7,"
elif localtime[0:3] == "Sun":
    thu = "Chủ nhật,"

if localtime[4:7] == "Jan":
    month_vn = "Tháng 1,"
elif localtime[4:7] == "Feb":
    month_vn = "Tháng 2,"
elif localtime[4:7] == "Mar":
    month_vn = "Tháng 3,"
elif localtime[4:7] == "Apr":
    month_vn = "Tháng 4,"
elif localtime[4:7] == "May":
    month_vn = "Tháng 5,"
elif localtime[4:7] == "Jun":
    month_vn = "Tháng 6,"
elif localtime[4:7] == "Jul":
    month_vn = "Tháng 7,"
elif localtime[4:7] == "Aug":
    month_vn = "Tháng 8,"
elif localtime[4:7] == "Sep":
    month_vn = "Tháng 9,"
elif localtime[4:7] == "Oct":
    month_vn = "Tháng 10,"
elif localtime[4:7] == "Nov":
    month_vn = "Tháng 11,"
elif localtime[4:7] == "Dec":
    month_vn = "Tháng 12,"

day_vn = "ngày " + localtime[8:10] + ","
nam = "năm " + localtime[-4:] 
gio = localtime[11:13] + " giờ,"
phut = localtime[14:16] + " phút,"
giay = localtime[17:19] + " giây,"

date_vn = gio +" " + phut +" " + giay +" " + thu + " " +day_vn + " " + month_vn +" " + nam
