print("""これは
        とても
        長いコード""")

#pythonには型指定の必要がない
z=100

#1
print("1")
print(2)
print(5+6)

#2
a = 10
b = 23
if a < 10:
    print("10未満です")
else:
    print("10以上です")

#3
if b <= 10:
    print("10以下です")
elif 10 < b and b <=25:
    print("10より大きく25以下です")
else:
    print("25より大きい")

#4
print(b%a)

#5
print(b//a)

#6
age = 20
if age < 20:
    print("未成年です")
else:
    print("成人です")


"""
これは
        とても
        長いコード
1
2
11
10以上です
10より大きく25以下です
3
2
成人です
"""