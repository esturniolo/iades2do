ltr = 50000
lpl = 15000
lpp = 5000
lpa = 2000
dessoc = 20
vtrdesfin = 0

itr = 0
ipl = 0
ipp = 1500
ipa = 700

cuantossocios = int(input("Cuantos socios en tribuna?:                        "))

vtr = int(input("Ingresar valor de la entrada a tribunas:                           "))
vpl = int(input("Ingresar valor de la entrada a plateas:                            "))
vpp = int(input("Ingresar valor de la entrada a plateas preferenciales:             "))
vpa = int(input("Ingresar valor de la entrada a palcos:                             "))


vtraux = vtr * dessoc / 100
vtrdes = int(vtr - vtraux)
vtrdesfin = vtrdesfin + vtrdes * cuantossocios

#print (str("---------------------"))
#print (int(vtrdesfin))
#print (str("---------------------"))


ttr = (ltr - itr) * vtr
ttrConSocios = ttr - vtrdesfin
tpl = (lpl - ipl) * vpl
tpp = (lpp - ipp) * vpp
tpa = (lpa - ipa) * vpa

tgr = ttrConSocios + tpl + tpp + tpa

print (str(ltr-itr).rjust(5), "entradas a tribunas : $ ",str(ttrConSocios).rjust(10))
print (str(lpl-ipl).rjust(5), "entradas a tribunas : $ ",str(tpl).rjust(10))
print (str(lpp-ipp).rjust(5), "entradas a tribunas : $ ",str(tpp).rjust(10))
print (str(lpa-ipa).rjust(5), "entradas a tribunas : $ ",str(tpa).rjust(10))
print ("TOTAL RECAUDACIÓN : $ ",str(tgr).rjust(12))
