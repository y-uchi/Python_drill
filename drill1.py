#Pythonではハッシュの値を格納する方法は、辞書(dictionary)を使用する

#辞書はキーと値のペアを保持する。

fruits = {} #空の辞書を用意

fruits['apple'] = 100
fruits['orange'] = 200
fruits['strawberry'] = 300

print(fruits) #辞書に格納されているキーと値を全て出力

price = fruits['apple']
print(price) # ['apple'](キー)に対応する値を呼び出し

# キーは一意である必要がある。同じキーに対して複数の値を関連づけることができない
# 存在しないキーで値を取得しようとするとkeyErrorが発生する。