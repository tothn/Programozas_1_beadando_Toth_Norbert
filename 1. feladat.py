n=int(input("körök száma: "))
lst_points=[]
lst_players=[]
for i in range(n):
    if n>1000:
        print("Túl sok kör!")
        break
    round=(n-(n-i))+1
    x,y=input().split()
    print("{}.kör: P1={} P2={}".format(round,x,y))
    x=int(x)
    y=int(y)
    if x>1000 or y>1000:
        print("Túl sok pont!")
        break
    if x>y:
        z=abs(x-y)
        print("Player One vezet {} ponttal.".format(z))
        lst_players.append("P1")
        lst_points.append(z)
    if y>x:
        z = abs(x - y)
        print("Player Two vezet {} ponttal.".format(z))
        lst_players.append("P2")
        lst_points.append(z)
    if x==y:
        print("Döntetlen, egyik játékos sem vezet!")
        lst_players.append("D")
        lst_points.append(0)

for i in range(n):
    if n>1000:
        break
    if n>len(lst_points):
        break
    z = max(lst_points)
    if lst_points[i]==z:
        print("\n{} nyert.".format(lst_players[i]))
        print("A legnagyobb különbség {} pont volt.".format(lst_points[i]))