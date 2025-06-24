def calc(d_calcul):
    for x in range(1,4):
        cons_kw=d_actuel[x]-d_preced[x]
        print('Abonne num',x,'KW consomme=',cons_kw)
        som_kw=d_calcul['p_kw']*cons_kw+d_calcul['abon']
        tva=som_kw*11/100
        som_net=som_kw+tva
        print('facutre de abonne num',x,'met payer en $',round(som_net,2))
d_preced={1:1234,2:213,3:1233}
d_actuel={1:1000,2:3312,3:1111}
taux_d=float(input("dollar "))
fuck=float(input("enter bills="))
prix_kw=float(input('electricty bills='))
d_calc={'t_d':taux_d,'abon':fuck,'p_kw':prix_kw}
calc(d_calc)