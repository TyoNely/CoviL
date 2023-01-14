from json import loads
from os import system,name
from time import sleep
#############
global RD,B,C,G
R='\033[0;31m';B='\033[1;34m';C='\033[1;37m';G='\033[1;32m'
#############
# O código pode não estar limpo, mas tá rápido.
# Vou recodar em JavaScript ou em Ruby quando eu tiver tempo.
#############
try:
	from requests import get
except:
	try:
		from sys import executable
		system(executable+' -m pip install requests')
		from requests import get
	except:
		print('%s[ %s!%s ] Instale manualmente o(s) módulo(s) requests.'%(R,R,));exit()
		
try:
	ipmenu=get('https://ipwhois.app/json/').text
	ipmenu=loads(ipmenu)
	ipmenu=ipmenu['ip']
except:
	print('%s[%s ! %s] Verifique sua conexão à Internet! \n%s'%(R,R,R))
	exit()

#Api Free pra quem quiser.
api={
'1':'https://brasilapi.com.br/api/ddd/v1/​',
'2':'https://www.receitaws.com.br/v1/cnpj/',
'3':'https://viacep.com.br/ws/',
'4':'https://ipwhois.app/json/',
'5':'https://brasilapi.com.br/api/banks/v1/',
'6':'https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/​',
'8':'https://lookup.binlist.net/',
'9':'https://www.consultacrm.com.br/api/',
'10':'http://ghostcenter.xyz/api/nome/'
}

'''
http://cnes.datasus.gov.br/pages/profissionais/consulta.jsp
'''

logo='''
 ▄▄·        ▌ ▐·▪  ▄▄▌  
▐█ ▌▪▪     ▪█·█▌██ ██•  
██ ▄▄ ▄█▀▄ ▐█▐█•▐█·██▪  
▐███▌▐█▌.▐▌ ███ ▐█▌▐█▌▐▌
·▀▀▀  ▀█▄▀▪. ▀  ▀▀▀.▀▀▀ 
 \n'''


########FUNÇÕES########
def req(api_req) -> str: return loads(get(api_req).text)
def clear(clean) -> None: return system(clean)
#######################
def cpf() -> str:
	result=loads(get(r'http://api.lkzn.tk/?token=9c06b7c4-627e-4b66-8837-f1b82c2c3854&cpfSimples='+input('%s%s%s\n%s>%s Digite o CPF : '%(R,logo,C,G,C)),verify=False).text)
	clear(clean)
	ban='%s%s%s\n'%(R,logo,C)
	try: return ban+'[ %sNome%s : %s ]\n[ %sCPF%s : %s ]\n[ %sAno de Nascimento%s : %s ]\n[ %sSexo %s: %s ]'%(G,C,result['msg']['nome'],G,C,result['msg']['cpf'],G,C,result['msg']['nascimento'],G,C,result['msg']['sexo'])
	except: return ban+'[ %s!%s ] CPF não encontrado.'%(R,C)

def ip() -> str:
	api_req=api['4']+input('%s%s%s\n%s>%s Digite o Endereço de IP que deseja buscar : '%(R,logo,C,G,C))
	result=req(api_req)
	try:
		return '[%s IP %s: %s ]\n[%s Tipo %s: %s ]\n[%s Continente%s: %s ]\n[%s País %s: %s ]\n[%s Capital %s: %s ]\n[%s Região %s: %s ]\n[%s Cidade %s: %s ]\n[%s DDI %s: %s ]\n[%s Latitude %s: %s ]\n[ %sLongitude%s : %s ]'%(G,C,result['ip'],G,C,result['type'],G,C,result['continent'],G,C,result['country'],G,C,result['country_capital'],G,C,result['region'],G,C,result['city'],G,C,result['country_phone'],G,C,result['latitude'],G,C,result['longitude'])
	except:
		return '%s[ %s!%s ] Endereço de IP não encontrado.'%(C,R,C)
#from time import sleep
def ddd() -> str:
	api_req=req('https://brasilapi.com.br/api/ddd/v1/%s'%input('%s%s%s\n%s>%s Digite o DDD : '%(R,logo,C,G,C)))
	clear(clean)
	try:
		msg='%s%s%s[ %sEstado%s: %s ]\n[ %sCidades%s:'%(R,logo,C,G,C,api_req['state'],G,C)
		for i in api_req['cities']: msg+=str(' '+G+i+','+C)
		return msg
	except Exception:
		#print(r)
		return '[ %s!%s ] DDD não Encontrado.'%(R,C)

def placa() -> str:
	result=loads(get('https://apicarros.com/v2/consultas/%s/f63e1e63dd231083d38ce929984aac7d'%input('%s%s%s\n%s>%s Digite a Placa : '%(R,logo,C,G,C)),verify=False).text)
	msg='%s%s%s\n'%(R,logo,C)
	clear(clean)
	for i in result:
		msg+=str('[ '+G+str(i.upper())+C+ ' : ' + str(result[i]) + ' ]\n').replace('{','\n')
	return msg

def nome() -> str:
	result='http://api.lkzn.tk/?token=9c06b7c4-627e-4b66-8837-f1b82c2c3854&nomeLkzn=%s'%input('%s%s%s\n%s>%s Digite o nome: '%(R,logo,C,G,C))
	result=req(result)
	msg=''
	try:
		for i in result['msg']:
			msg+='''\n[ %sCPF%s : %s ]\n[ %sNome%s : %s ]\n[ %sNascimento%s : %s ]\n[ %sGênero%s : %s ]
'''%(G,C,i['cpf'],G,C,i['nome'],G,C,i['nascimento'],G,C,i['sexo'])
	except Exception as e:
			msg='[ %s!%s ] Nome inválido ou pequeno demais.'%(R,C)
	return msg
def cep() -> str:
	try:
		result=req(api['3']+input('%s%s%s\n%s>%s Digite o CEP : '%(R,logo,C,G,C))+'/json')
		return '[ %sCEP%s : %s ]\n[ %sLogradouro%s : %s]\n[ %sComplemento%s : %s ]\n[ %sBairro%s : %s]\n[ %sLocalidade%s : %s]\n[ %sEstado(UF)%s : %s]\n[ %sIBGE%s : %s]\n[ %sGIA%s : %s]\n[ %sDDD%s : %s]\n[ %sSIAFI%s : %s]'%(G,C,result['cep'],G,C,result['logradouro'],G,C,result['complemento'],G,C,result['bairro'],G,C,result['localidade'],G,C,result['uf'],G,C,result['ibge'],G,C,result['gia'],G,C,result['ddd'],G,C,result['siafi'])
	except:
		error ='[ %s!%s ] CEP Inválido.'%(R,C)
		return error

def covid() -> str:
	result=req(str("https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/")+str(input('%s%s\n%s>%s Digite o UF : '%(R,logo,G,C))))
	try: return '[ %sEstado%s : %s ]\n[ %sCasos%s : %s ]\n[ %sMortes%s : %s ]\n[ %sSuspeitas%s : %s ]\n[ %sCasos Recusados%s : %s]'%(G,C,result['state'],G,C,result['cases'],G,C,result['deaths'],G,C,result['suspects'],G,C,result['refuses'])
	except Exception: return '[ %s!%s ] Nenhum resultado encontrado para esse UF.'%(R,C)
	
def bank() -> str:
	result=req(api['5']+input('%s%s%s\n%s>%s Digite o código bancário : '%(R,logo,C,G,C)))
	try: return '[ %sISPB%s : %s ]\n[ %sNome%s : %s ]\n[ %sCódigo%s : %s ]\n[ %sNome Completo%s : %s ]'%(G,C,result['ispb'],G,C,result['name'],G,C,result['code'],G,C,result['fullName'])
	except Exception: return '[ %s!%s ] Código bancário inválido.'%(R,C)

def bin() -> str:
	try: result=req('https://lookup.binlist.net/%s'%input('%s%s%s\n%s>%s Digite a BIN : '%(R,logo,C,G,C)));return '[ %sTipo%s : %s ]\n[ %sMarca%s : %s ]\n[ %sPré-Pago%s : %s ]\n[ %sPaís%s : %s ]\n[ %sNome do Banco%s : %s ]\n[ %sTelefone%s : %s ]\n[ %sCidade%s : %s ]'%(G,C,result['type'],G,C,result['brand'],G,C,str(result['prepaid']),G,C,result['country']['name'],G,C,result['bank']['name'],G,C,result['bank']['phone'],G,C,result['bank']['city'])
	except: return '[ %s!%s ] BIN Inválida.'%(R,C)

def cnpj() -> str:
	# preguica ativada
	result=req('https://www.receitaws.com.br/v1/cnpj/%s'%input('%s%s%s\n%s>%s Digite o CNPJ : '%(R,logo,C,G,C)))
	msg=''
	for i in result:
		msg+=str('[ '+G+str(i.upper())+C+ ' : ' + str(result[i]) + ' ]\n')
	return msg

grupo_dict={
'Grupo do Discord': 'https://discord.gg/R76ZeUqbYJ',
'Tik Tok':'https://www.tiktok.com/@nelytrem',
'Twitter Dos Adm': 'https://twitter.com/NelyTrem | https://twitter.com/Karamujo1337',
'Youtube Dos Adm': 'https://www.youtube.com/@NelyTrem'}

def grupo() -> str:
	msg=''
	for i in grupo_dict: msg+=str('{ '+G+str(i)+G+' : '+str(grupo_dict[i])+C+' }\n')
	input('%s%s%s\n%s%s'%(R,logo,C,msg,'%s<%s Aperte Enter para voltar ao Menu. %s>%s'%(G,C,G,C)))
	
#######################
def exit() -> None:
	global Exit
	Exit=True

def show_api() -> str:
	msg=''
	for i in api: i='%s{%s '%(R,C)+api[i]+' %s}%s\n'%(R,C);msg+=i
	input('%s%s%s\n === Lista de APIs ===\n%s%s<%s APERTE ENTER PARA VOLTAR AO MENU %s>%s'%(R,logo,C,msg,G,C,G,C))

Exit=False

MatchCase={
'1':ddd,
'2':cnpj,
'3':cep,
'4':ip,
'5':bank,
'6':covid,
'7':placa,
'8':bin,
'9':cpf,
'10':nome}
MatchCase_Function={
'12':grupo,
'11':show_api,
'00':exit
}

def menu() -> None:
	while Exit==False:
		clear(clean)
		option=str(input('''%s%s%s
Bem-Vindo(a) ao %sCoviL%s
Seu Endereço de IP : %s%s%s

%s[%s BY : %sCoded by Nely %s]

[Twitter : %s@NelyTrem @Karamujo1337%s | Discord : %shttps://discord.gg/R76ZeUqbYJ%s]

|────────▸Consulta◂──────────|
| { %s1%s } Consulta de DDD      |    
| { %s2%s } Consulta de CNPJ     |   
| { %s3%s } Consulta de CEP      |  
| { %s4%s } Consulta de IP       |  
| { %s5%s } Consulta Bancária    | 
| { %s6%s } Covid-19             |
| { %s7%s } Consulta de Placa    |
| { %s8%s } Consulta de BIN      |
| { %s9%s } Consulta de CPF      |
| { %s10%s } Consulta de Nome    |
|──────────▸Extra◂───────────|
| { %s11%s } APIs                |
| { %s12%s } Redes Sociais       |
| { %s00%s } Sair                |
|───────────▸|Fim|◂──────────|

>>> %s'''%(R,logo,C,R,C,R,ipmenu,C,C,C,R,C,R,C,R,C,R,C,R,C,R,C,R,C,R,C,R,C,R,C,R,C,R,C,R,C,R,C,R,C,R,C,R)))
		clear(clean)
		try:
			res='%s\n%s'%(MatchCase[option](),'%s<%s Aperte Enter para retornar ao menu %s>%s'%(G,C,G,C))
			input(res)
		except Exception:
			try:
				MatchCase_Function[option]()
			except:
				pass
if __name__=='__main__':
	global clean
	clean ={'nt':'cls','posix':'clear'}[name]
	menu()
