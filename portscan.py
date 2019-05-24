#importação das libs necessarias para realização do processo
import sys
import socket
import subprocess

#solicita a URL a ser scanneada
url = input("Informe a URL: ")
#recupera ip referente a URL
pegaip = socket.gethostbyname(url)

#cria txt com o resultado do processo
criatxt = open('resultadoportscan.txt', 'w')	
criatxt.write('RESULTADO DO PORTSCAN REALIZADO NA URL: ' + url + '\n')
criatxt.write('\n')
criatxt.close()

try:
	#percorre as portas da 1 até a 1025 
	for porta in range(1,1025):  		
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		retorno = sock.connect_ex((pegaip, porta))
		#verifica o retorno
		if retorno == 0:			
			gravaresltado = open('resultadoportscan.txt', 'a')	
			gravaresltado.write('Porta ' + str(porta) + ' : Aberta \n')
			gravaresltado.close()
			print('Porta ' + str(porta) + ' : Aberta')
		else:
			print('Porta ' + str(porta) + ' : Fechada')
		sock.close()

#tratamento de exceções
except socket.gaierror:
    print('Nome do host não pôde ser resolvido, processo finalizado.')
    sys.exit()

except socket.error:
    print('Não foi possível conectar ao servidor, processo finalizado')
    sys.exit()
	
except KeyboardInterrupt:
    print('Você apertou Ctrl+C, processo finalizado.')
    sys.exit()

print('Portscan finalizado')