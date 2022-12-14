import re
txt = "Hanoror bought 5 portions of orange soil for 13.50 EUR."
out = re.findall("..\.", txt)
print(out)

txt = "jox r.nohre@jth.hj.se, bjox@se, adam@example.com, jox@jox@jox.com."

out = re.findall("[\w\.]+@\w+\.[\.\w]+\w", txt)

print(out)

f = open("tabla.html", encoding="utf-8")
txt = f.read()
print(txt)