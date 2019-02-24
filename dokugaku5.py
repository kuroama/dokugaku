#1
like_musician = ["arashi","smap"]

#2
visited_place = ([35.658581,139.745433],[35.681236,139.767125],)

#3
personal = {"like_color":"red","height":170}

#4
value = input("input key:")
if value in personal:
    print(personal[value])

#5
like_musician_songs = {"嵐":["Love so sweet","truth","Beautiful days"],"SMAP":["世界に一つだけの花","夜空ノムコウ"]}

#6
s = set([1,2,3,4,1,3,2])

print(like_musician)
print(visited_place)
print(personal)
print(like_musician_songs)
print(s)

"""
input key:height
170
['arashi', 'smap']
([35.658581, 139.745433], [35.681236, 139.767125])
{'like_color': 'red', 'height': 170}
{'嵐': ['Love so sweet', 'truth', 'Beautiful days'], 'SMAP': ['世界に一つだけの花', '夜空ノムコウ']}
{1, 2, 3, 4}
"""