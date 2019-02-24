#1
kamu = "カミュ"
for k in kamu:
    print(k)

#2
what = input("何を書いた？")
who = input("誰に書いた？")
print("私は昨日{}を書いて、{}に送った!".format(what,who))

#3
str3 = "aldous Huxley was born in 1894."
print(str3.capitalize())

#4
str4 = "どこで？　だれが？　いつ？"
print(str4.split("　"))

#5
list5 = ["The","fox","jumped","over","the","fance","."]
print(" ".join(list5[:-1])+list5[-1])

#6
str6 = "A screaming comes across the sky."
print(str6.replace("s","$"))

#7
str7 = "Hemingway"
print(str7.index("m"))

#8
print("彼はわたしに\"ありがとう\"と言った")

#9
three_str = " three"
print((three_str+three_str+three_str).strip())
print((3*three_str).strip())

#10
str10 = "四月の晴れた寒い日で、時計がどれも十三時を打っていた。"
print(str10[0:10])

"""
カ
ミ
ュ
何を書いた？手紙
誰に書いた？祖母
私は昨日手紙を書いて、祖母に送った!
Aldous huxley was born in 1894.
['どこで？', 'だれが？', 'いつ？']
The fox jumped over the fance.
A $creaming come$ acro$$ the $ky.
2
彼はわたしに"ありがとう"と言った
three three three
three three three
四月の晴れた寒い日で
"""