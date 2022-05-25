from cgitb import text
import requests as rq
import webbrowser as web 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from os import link
from selenium.webdriver.chrome.options import Options
import pyautogui
import speech_recognition as sr



version = "0.1.5"
cidade = 'recife'
navegador = "C:\Program Files\Google\Chrome\Application\chrome.exe  %s"


def intro():
	msg = "Assistente - version {} / by: João Boudoux".format(version)
	print("-" * len(msg) +  "\n{}\n".format(msg)  +   "-" * len(msg))


lista_erros = [
		"Não entendi nada",
		"Desculpe, não entendi",
		"Repita novamente por favor"
]


conversas = {
	#Inicio de conversa
	"Oi": "Olá, tudo bem?",
	"oi": "Olá, tudo bem?",
	"olá": "Oi tudo bem?",
	"Olá": "Oi, tudo bem?",
	"Eae": "Olá, tudo bem?",
	"eae": "Oi, tudo bem?",
	"E aí": "Olá, tudo bem?",
	"e aí": "Olá, como vai?",
	"Opa tudo beleza": "Olá, tudo sim e você?",
	"opa tudo beleza": "Tudo sim e você?",
	"Oi Chloe": "Olá, tudo bem?",  "Oi chloe": "Oi, tudo bem?",
	"oi Chloe": "Olá, tudo bem?",  "oi chloe": "Oi, tudo bem?",
	"Oi Cloe": "Oi, tudo bem?",    "Oi cloe": "Oi, tudo bem?",
	"oi Cloe": "Oi, tudo bem?",    "oi cloe": "Oi, tudo bem?",
	"Olá Chloe": "Olá, tudo bem?", "Olá chloe": "Olá, tudo bem?",
	"olá Chloe": "Olá, tudo bem?", "olá chloe": "Olá, tudo bem?",
	"Olá Cloe": "Oi, tudo bem?",   "Olá cloe": "Oi, tudo bem?",
	"olá Cloe": "Oi, tudo bem?",   "olá cloe": "Oi, tudo bem?",

    #Intermedio
	"Tudo tranquilo": "Fico feliz em saber",
	"tudo tranquilo": "Fico feliz em saber",
	"Tudo ótimo": "Que bom, fico feliz em saber",
	"tudo ótimo": "Que bom, fico feliz em saber",
	"Tudo sim e você": "Estou bem, obrigada por perguntar",
	"tudo sim e você": "Estou bem, obrigada por perguntar",
	"Sim e você": "Estou bem, obrigado por perguntar",
	"sim e você": "Estou bem, obrigado por perguntar",
	"Sim": "Magnifico, em que posso te ajudar?",
	"sim": "Maneiro, em que posso te ajudar?",
	"Não": "Que pena, em que posso te ajudar?",
	"não": "Sinto muito, em que posso te ajudar?",
	"Não e você": "Estou funcionando corretamente, em que posso te ajudar?",
	"não e você": "Meus sistemas estão operantes, em que posso te ajudar?",
	"Infelizmente não": "Que pena, em que posso te ajudar?",
	"infelizmente não": "Que pena, em que posso te ajudar?",
	"Estou bem": "Fico feliz em saber, em que posso te ajudar?",
	"estou bem": "Legal, em que posso te ajudar?",
	"Estou bem e você": "Perfeitamente bem, em que posso te ajudar?",
	"estou bem e você": "Estou otima, obrigado por perguntar",
	"Estou triste": "Sinto muito, o que posso fazer para melhorar o seu dia?",
	"estou triste": "Sinto muito, o que posso fazer para melhorar o seu dia?",
	"Estou triste e você": "Estou funcionando corretamente, o que posso fazer para melhorar o seu dia?",
	"estou triste e você": "Estou funcionando corretamente, o que posso fazer para melhorar o seu dia?",

	#Perguntas

	"Quem te criou": "Eu tenho um papai e uma mamãe, eles se chamam João e Myllena",
	"quem te criou": "Eu tenho um papai e uma mamãe, eles se chamam João e Myllena",
	"Quem criou você": "Eu tenho um papai e uma mamãe, eles se chamam João e Myllena",
	"quem criou você": "Eu tenho um papai e uma mamãe, eles se chamam João e Myllena",
	"Quem é você": "Eu sou um código feito para ajudar, mas na vida real eu sou uma linda cachorrinha",
	"quem é você": "Eu sou um código feito para ajudar, mas na vida real eu sou uma linda cachorrinha",
	"Qual é o seu nome": "Eu me chamo Chloe, minha mãe Myllena me deu esse nome",
	"qual é o seu nome": "Eu me chamo Chloe, minha mãe Myllena me deu esse nome",
	"Qual o seu nome": "Eu me chamo Chloe, minha mãe Myllena me deu esse nome",
	"qual o seu nome": "Eu me chamo Chloe, minha mãe Myllena me deu esse nome",
	"Quantos anos você tem": " Estou na minha versão " + version + " E ainda tenho muito para viver ",
	"quantos anos você tem": " Estou na minha versão " + version + " E ainda tenho muito para viver ",
	"O que você pode fazer": "Eu tenho várias funcionalidades que você pode encontrar, veja no manual algumas delas",
	"o que você pode fazer": "Eu tenho várias funcionalidades que você pode encontrar, veja no manual algumas delas",
	"Você tem sentimentos": "Não tenho capacidade de sentir algo, mas minha versão cachorrinha ama muito papai e mamãe",
	"você tem sentimentos": "Não tenho capacidade de sentir algo, mas minha versão cachorrinha ama muito papai e mamãe",


    #Agradecimentos
	"Obrigado": "Não tem de que",
	"obrigado": "Não precisa agradeçer",
	"Muito obrigado": "Estou feliz em ajudar",
	"muito obrigado": "Fico feliz por ajudar",
	"Muitíssimo obrigado": "Não precisa agradecer",
	"muitíssimo obrigado": "Estou aqui para o que precisar",
	"Tamo junto": "É isso ai, disponha",
	"tamo junto": "É isso ai, disponha",
	"Valeu": "De nada",
	"valeu": "Disponha",
	"É nós": "Tamo junto",
	"é nós": "Tamo junto",

}

comandos = {
	"desligar": "desligando",
	"reiniciar": "reiniciando"
}


def verifica_nome(user_name):
	if user_name.startswith("Meu nome é"):
		user_name = user_name.replace("Meu nome é", "")
	if user_name.startswith("Eu me chamo"):
		user_name = user_name.replace("Eu me chamo", "")
	if user_name.startswith("Eu sou o"):
		user_name = user_name.replace("Eu sou o", "")
	if user_name.startswith("Eu sou a"):
		user_name = user_name.replace("Eu sou a", "")

	return user_name 


def  verifica_nome_exist(nome):
	dados = open("IAChloe/dados/nomes.txt", "r")
	nome_list = dados.readlines()

	if not nome_list:
		vazio = open("IAChloe/dados/nomes.txt", "r")
		conteudo = vazio.readlines()
		conteudo.append("{}".format(nome))
		vazio = open("IAChloe/dados/nomes.txt", "w")
		vazio.writelines(conteudo)
		vazio.close()

		return "Olá {}, prazer em te conhecer!".format(nome)

	for linha in nome_list:
		if linha == nome:
			return "Olá {}, acho que já nos conhecemos".format(nome)

	vazio = open("IAChloe/dados/nomes.txt", "r")
	conteudo = vazio.readlines()
	conteudo.append("\n{}".format(nome))
	vazio = open("IAChloe/dados/nomes.txt", "w")
	vazio.writelines(conteudo)
	vazio.close()

	return "Oi {} é a primeira vez que nos falamos".format(nome)


def name_list():
	try:
		nomes = open("IAChloe/dados/nomes.txt", "r")
		nomes.close()

	except FileNotFoundError:
		nomes = open("IAChloe/dados/nomes.txt", "w")
		nomes.close()


def calcula(entrada):
	if "mais" in entrada or "+" in entrada:
		# É soma
		entradas_recebidas = entrada.split(" ")
		resultado = int(entradas_recebidas[1]) + int(entradas_recebidas[3])

	elif "menos" in entrada or "-" in entrada:
		# É subtração

		entradas_recebidas = entrada.split(" ")
		resultado = int(entradas_recebidas[1]) - int(entradas_recebidas[3])

	elif "vezes" in entrada or "x" in entrada:
		# É vezes

		entradas_recebidas = entrada.split(" ")
		resultado = round(float(entradas_recebidas[1]) * float(entradas_recebidas[3]), 2)

	elif "dividido" in entrada or "/" in entrada:
		# É divisão

		entradas_recebidas = entrada.split(" ")
		resultado = round(float(entradas_recebidas[1]) / float(entradas_recebidas[4]), 2)

	else:

		resultado = "Operação não encontrada"


	return resultado



def clima_tempo():	
	endereco_api = "http://api.openweathermap.org/data/2.5/weather?appid=a7ae64dcbf0c17c36cbf714ec6614cf7&q="
	url = endereco_api + cidade

	infos = rq.get(url).json()


	# Coord
	longitude = infos['coord']['lon']
	latitude = infos['coord']['lat']
	# main
	temp = infos['main']['temp'] - 273.15 # Kelvin para Celsius
	pressao_atm = infos['main']['pressure'] / 1013.25 #Libras para ATM
	humidade = infos['main']['humidity'] # Recebe em porcentagem
	temp_max= infos['main']['temp_max'] - 273.15 # Kelvin para Celsius
	temp_min = infos['main']['temp_min'] - 273.15 # Kelvin para Celsius

	#vento
	v_speed = infos['wind']['speed'] # km/ h
	v_direc = infos['wind']['deg'] #Recebe em graus

	#clouds / nuvens

	nebulosidade = infos['clouds']['all']

	#id
	id_da_cidade = infos['id']

	# 11
	return [longitude, latitude, 
		temp, pressao_atm, humidade, 
		temp_max, temp_min, v_speed, 
		v_direc, nebulosidade, id_da_cidade]


def temperatura():
	temp_atual = clima_tempo()[2]
	temp_max = clima_tempo()[5]
	temp_min = clima_tempo()[6]
	
	return [temp_atual, temp_max, temp_min]



def abrir(fala):
	try:
		if "Google" in fala:
			web.get().open("Http://www.google.com.br/")
			return "abrindo google"

		elif "YouTube" in fala:
			web.get().open("Http://www.youtube.com.br/")
			return "abrindo youtube"

		else:
			return "site não cadastrado"
	except:
		return "houve um erro"
		
def search(fala):
 rec = sr.Recognizer()

 with sr.Microphone() as source:
  rec.adjust_for_ambient_noise(source)
  audio = rec.listen(source)
  procurar = rec.recognize_google(audio, language="pt")
  chrome_options = Options()
  chrome_options.add_experimental_option("detach", True)
  navegador = webdriver.Chrome(options= chrome_options)
  navegador.get('https://www.google.com.br/')
  digitar = navegador.find_element_by_name('q')
  digitar.send_keys(procurar)
  digitar.submit() 
  print("Procurando por: " + procurar)
  return 'Aqui está o que encontrei sobre: ' + procurar
 

