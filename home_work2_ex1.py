"""
כתוב תוכנית שמקבלת מהמשתמש את חום גופו (במעלות צלזיוס)
אם החום מעל 38, הדפס "חום גבוה".
אם החום בין 36 ל-38 כולל, הדפס "חום תקין".
אחרת, הדפס "חום נמוך

"""
print("welcome to our hospital")
celsius = float(input("please enter your tem body"))
if celsius>38:
    print("high body temp!")
elif 36<= celsius<38:
    print("good!")
else:
    print("low body temp")