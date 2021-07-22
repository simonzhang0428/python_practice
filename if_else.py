weather = "sunny"
date = "Sun."
is_holiday = False
if weather == "sunny" and (is_holiday or date in ["Sat.", "Sun."]):
    print("Go play outside")
elif not is_holiday and date not in ["Sat.", "Sun."]:
    print("Go to work")