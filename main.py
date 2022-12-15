import re

txt = "Hanoror bought 5 portions of orange soil for 13.50 EUR."
out = re.findall("..\.", txt)
print(out)

# Task 1

txt = "jox r.nohre@jth.hj.se, bjox@se, adam@example.com, jox@jox@jox.com."

out = re.findall("\w[\w\.]+\w@\w+(?:\.\w+)+\w", txt)

print(out)

# Task 2

out = re.findall("(?:^|\s)(\w[\w\.]+\w@\w+(?:\.\w+)+\w)", txt)

print(out)

# Task 3

htmltxt = """ bla bla bla
    <h1> My Rubric   </h1>
    bla bla bla. """

out = re.findall("<h1>\s*(.*?)\s*</h1>", htmltxt)

print(out)

# Main Task

f = open("tabla.html", encoding="utf-8")
txt = f.read()
#print(txt)

times = re.findall(r'<td class="svtTablaTime">\s*(\d+\.\d+)\s*</td>\s*<td.*?>\s*<h4.*?>\s*Simpsons\s*</h4>', txt)
out = re.findall(r'<h4.*?>\s*Simpsons\s*</h4>',txt)
descriptions = re.findall(r'<td.*?>\s*(\d+\.\d+)\s*</td>\s*<td.*?>\s*<h4.*?>\s*Simpsons\s*</h4>(?:\s*<div.*?>){3}\s*<p.*?>\s(.*?Säsong\s(\d+).\sDel\s(\d+)\sav\s(\d+).*)\s</p>', txt)

print(times)
print(out)
for item in descriptions:
    print("----------------------")
    print(f"Tid: {item[0]}")
    print(f"Säsong: {item[2]}")
    print(f"Avsnitt: {item[3]} av {item[4]}")
    print(f"Handling: {item[1]}")
print("----------------------")