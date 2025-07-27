"""
כתוב תוכנית שמקבלת סיסטולי ודיאסטולי (שני מספרים)
אם סיסטולי מעל 140 או דיאסטולי מעל 90, הדפס "לחץ דם גבוה".
אחרת, הדפס "לחץ דם תקין

"""
sistoli = int(input("please enter sistoli value:"))
distoli = int(input("please enter distoli value:"))
if sistoli > 140 or distoli > 90:
    print(f"high blood presser, your value:\nsistoly:{sistoli}, distoli:{distoli}")
else:
    print(f"good blood presser, your value:\nsistoly:{sistoli}, distoli:{distoli}")
