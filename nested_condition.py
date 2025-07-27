temperature = float(input("Enter your body temp:"))
cough = input("Do you have a cough?(yes/no)")
shortness_of_breath = input("Do you have shortness of breath?(yes/no)")
if temperature >= 38:
    if cough == "yes":
        if shortness_of_breath == "yes":
            print("Possible serious respiratory infection")#temp> 38 and cough and shortness
        else:
            print("Possible flu or mild respiratory infection")#temp>38 and cough and no shortness
    else:
        print("possible non respiratory infection")#temp >38 no cough
else:
    if cough =="yes":
        print("take kal garon!")#temp<38 and cough
    else:
        print("have a good day!")#temp <38 and no cough


print("make happen any way")
