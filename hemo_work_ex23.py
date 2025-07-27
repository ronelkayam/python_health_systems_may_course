"""
	לכל חולה נמדד לחץ דם פעמיים ביום למשך 3 ימים.
	 חשב עבור כל חולה את ההפרש המקסימלי בין המדידות באותו יום,
	 והצג את החולה עם הסטייה הכי גדולה.
"""

# מדידות לחץ דם - חולה 1
p1_id = 222333444
p1_d1_m1 = 120
p1_d1_m2 = 130
p1_d2_m1 = 125
p1_d2_m2 = 140
p1_d3_m1 = 130
p1_d3_m2 = 128

# חולה 2
p2_id = 111222333
p2_d1_m1 = 110
p2_d1_m2 = 115
p2_d2_m1 = 112
p2_d2_m2 = 118
p2_d3_m1 = 117
p2_d3_m2 = 122

# חולה 3
p3_id = 666777888
p3_d1_m1 = 135
p3_d1_m2 = 160
p3_d2_m1 = 140
p3_d2_m2 = 138
p3_d3_m1 = 145
p3_d3_m2 = 155

# מחשבים הפרשים יומיים לכל חולה
p1_diff1 = abs(p1_d1_m1 - p1_d1_m2)
p1_diff2 = abs(p1_d2_m1 - p1_d2_m2)
p1_diff3 = abs(p1_d3_m1 - p1_d3_m2)
p1_max = max(p1_diff1, p1_diff2, p1_diff3)

p2_diff1 = abs(p2_d1_m1 - p2_d1_m2)
p2_diff2 = abs(p2_d2_m1 - p2_d2_m2)
p2_diff3 = abs(p2_d3_m1 - p2_d3_m2)
p2_max = max(p2_diff1, p2_diff2, p2_diff3)

p3_diff1 = abs(p3_d1_m1 - p3_d1_m2)
p3_diff2 = abs(p3_d2_m1 - p3_d2_m2)
p3_diff3 = abs(p3_d3_m1 - p3_d3_m2)
p3_max = max(p3_diff1, p3_diff2, p3_diff3)

# השוואת הסטיות בין החולים
if p1_max >= p2_max and p1_max >= p3_max:
    print(f"Patient with the greatest deviation is {p1_id}, the deviation :{p1_max}")
elif p2_max >= p1_max and p2_max >= p3_max:
    print(f"Patient with the greatest deviation is {p2_id}, the deviation :{p2_max}")
else:
    print(f"Patient with the greatest deviation is {p3_id}, the deviation :{p3_max}")

