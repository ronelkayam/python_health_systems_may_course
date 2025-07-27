"""
כתוב לולאה שמדפיסה את הכמות המצטברת של תרופה אם נותנים מנה שביום הראשון תהיה 2 מ"ג
  וביום האחרון ־20 מ"ג.
כאשר מגדילים את המינון ב2 מ"ג ליום
"""
start_dosage = 2
stop_dosage = 20
increase = 2
sum = 0
for dosage in range(start_dosage, stop_dosage+1, increase):
    #range created - 2,4,6,8,10,12,14,16,18,20
    sum += dosage
print(f"dosage sum:{sum}")
