#1
list1=["ウォーキング・デッド","アントラージュ","ザ・ソプラノズ","ヴァンパイア・ダイアリーズ"]
for title in list1:
    print(title)

#2
for i in range(25,50):
    print(i)

#3
for i,title in enumerate(list1):
    print(str(i)+":"+title)

#4
while True:
    num_list = [1,5,7,34,9]
    str = input("文字を入力してください:")
    if str == "q":
        break
    if str.isdigit():
        if int(str) in num_list:
            print("正解")
        else:
            print("不正解")
    else:
        print("数字を入力するか、qで終了します")

#5
list5_1 = [8,19,148,4]
list5_2 = [9,1,33,83]
added = []
for i in list5_1:
    for j in list5_2:
        added.append(i*j)

print(added)

"""
ウォーキング・デッド
アントラージュ
ザ・ソプラノズ
ヴァンパイア・ダイアリーズ
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
0:ウォーキング・デッド
1:アントラージュ
2:ザ・ソプラノズ
3:ヴァンパイア・ダイアリーズ
文字を入力してください:1
正解
文字を入力してください:2
不正解
文字を入力してください:1.2
数字を入力するか、qで終了します
文字を入力してください:q
[72, 8, 264, 664, 171, 19, 627, 1577, 1332, 148, 4884, 12284, 36, 4, 132, 332]
"""