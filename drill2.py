# 辞書の多重構造
# あるキーの中にも辞書が存在する状態、いわゆる多次元の辞書の状態もある

monster = {"fire_dragon":{"Rioleia":"雷"}, "thounder_wolf":{"Zinogre":"氷"}} #火竜というキーにリオレイアというキーが入っている
monster["fire_dragon"]["Rioleus"] = "龍"  #リオレイアだけでなくリオレウスも火竜という辞書の中に要素を追加した

print(monster) #ハッシュに入っているもの全てを表示

karyuu = monster['fire_dragon'] #一つ目のキーにネストされているもの全てを変数karyuuに定義
print(karyuu) # karyuuで定義された全てのハッシュ化情報を出力
weekness = monster['fire_dragon']['Rioleia'] # ネストされているキーを指定するには、まずネストされているキーを呼び出し、更にネストされているキーも呼び出して定義する
print(weekness) # ネストされているキーの値が変数定義されているため、リオレイやの弱点として情報が出力される