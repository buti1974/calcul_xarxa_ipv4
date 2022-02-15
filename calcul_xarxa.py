ip=[0,0,0,0]
ip_inv=[255,255,255,255]
ip_mascara=[255,255,255,255]

#torna de 0 a 255 segons els 8 bits
def part_mascara(bits):
	resultat=0
	for i in range(0,bits):
		resultat=resultat+pow(2,7-i)
	return resultat

#or binari de les ips
def or_binari(ip1,ip2):
	resultat=[0,0,0,0]
	for i in range(0,4):
		resultat[i]=ip1[i]|ip2[i]
	return resultat

#or binari de les ips
def and_binari(ip1,ip2):
	resultat=[0,0,0,0]
	for i in range(0,4):
		resultat[i]=ip1[i]&ip2[i]
	return resultat

#convertim array int d'ip a string
def ip_a_string(ip):
	return str(ip[0])+"."+str(ip[1])+"."+str(ip[2])+"."+str(ip[3])

def calcul_xarxa():
	ip_address=input("Entri l'adreça de xarxa: ")
	bits=int(input("Entri els bits de màscara: "))
	ip_address=ip_address.split(".")
	for i in range(0,4):
		ip[i]=int(ip_address[i])
	for i in range(0,4):
		if bits >= ((i+1)*8):
			ip_mascara[i]=255
		else:
			ip_mascara[i]=part_mascara(8-(((i+1)*8)-bits))
		ip_inv[i]=ip_inv[i]-ip_mascara[i]
	primera_ip=and_binari(ip,ip_mascara)
	ultima_ip=or_binari(ip,ip_inv)
	resposta="\nResultat\nMascara: "+ip_a_string(ip_mascara)
	resposta=resposta+"\nNombre maxim equips per xarxa: "+str(pow(2, 32-bits)-2)
	resposta=resposta+"\nIP de xarxa: "+ip_a_string(primera_ip)
	resposta=resposta+"\nIP de broadcast: "+ip_a_string(ultima_ip)
	primera_ip[3]=primera_ip[3]+1
	ultima_ip[3]=ultima_ip[3]-1
	resposta=resposta+"\nPrimera IP: "+ip_a_string(primera_ip)
	resposta=resposta+"\nUltima IP: "+ip_a_string(ultima_ip)
	return resposta

print (calcul_xarxa())
