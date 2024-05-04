# Автор Ігор Хруневич
# Цю міні-програму створено, щоб зацікавити дітей програмуванням
# Користуйтесь, вивчайте, досліджуйте, змінюйте - експериментуйте

a = float(input("Введіть доданок 1 = "))
b = float(input("Введіть доданок 2 = "))
j = float(input("Введіть доданок 3 , якщо нема введіть 0 = "))
p = float(input("Введіть доданок 4 , якщо нема введіть 0  = "))

print (" ")
print ("Д О Д А Є М О   В   С Т О В П Ч И К")
print (" ")

c = len(str(abs(a)))-len(str(abs(b)))
k = len(str(abs(a)))-len(str(abs(j)))
r = len(str(abs(a)))-len(str(abs(p)))
d = c+1
q = k+1
s = r+1
e = len(str(abs(a)))

print (' ', a)
print (' '*d, b)
print (' '*q, j)
print (' '*s, p)
print (' ','-' * e)
print (' ',a+b+j+p)





