number=int(input("Plz enter total number of students: "))
sum=float(0.0)                           # مقدار اولیه جمع کل را برابر صفر قرار میدهد
for i in range(1,number+1):
  grade=float(input("Plz enter grade of student No. "+str(i)+": "))
  sum+=grade                             # در هر تکرار مقدار وارد شده را به جمع کل اضافه میکند
  if i==1:                               # پس از خواندن اولین  مقدار ماکزیمم و مینمم را برابر آن قرار میدهد
    max=grade
    min=grade
  else:                                  # در تکرارهای دوم به بعد
    if grade>max:                        # اگر عدد وارد شده بزرگتر از ماکزیمم باشد، آنرا در ماکزیمم قرار میدهد
      max=grade
    else:                                # در غیر اینصورت، اگر مقدار وارد شده کوچکتر از مینیمم باشد، آنرا در مینیمم قرار میدهد
      if grade<min:
        min=grade
average=sum/number                       # برای محاسبه میانگین، جمع کل اعداد را بر تعداد آنها تقسیم میکند
print("Aaverage= ",average)              # چاپ مقدار میانگین
print("Max= ",max)                       # چاپ مقدار ماکزیمم
print("Min= ",min)                       # چاپ مقدار مینیمم
  

