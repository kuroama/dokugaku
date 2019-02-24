import csv
#1
with open("Hello_world.txt","r",encoding="utf-8") as f:
    print(f.read())

#2
answer = input("出身地はどこですか:")
with open("Answer.txt","w",encoding="utf-8") as f:
    f.write(answer)

#3
data3 = [["Top Gun","Risky Business","Minority Report"],["Titanic","The Revenant","Inception"],["Training Day","Man on Fire","Flight"]]
with open("data3.csv","w",newline="",encoding="utf-8") as f:
    w = csv.writer(f,delimiter=",")
    for i in data3:
        w.writerow(i)
    
#4
data4 = [["トップガン","リスキービジネス","マイノリティーリポート"],["タイタニック","レヴェナント","インセプション"],["トレーニングデー","マイ・ボディーガード","フライト"]]
with open("data4.csv","w",newline="",encoding="utf-8") as f:
    w = csv.writer(f,delimiter=",")
    for i in data4:
        w.writerow(i)
    

"""
Hello world!
出身地はどこですか:Tokyo
"""