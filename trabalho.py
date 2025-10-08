import os

lista_pacientes = []

def exibir_titulo():
	print('ℂ𝕝𝕚́𝕟𝕚𝕔𝕒 𝕍𝕚𝕕𝕒+')
	print()

def exibir_cabecalho_menu():
	print('===SISTEMA CLÍNICA VIDA+===')
	print()

def exibir_subtitulo(texto):
	os.system('cls')
	linha = '*' * (len(texto))
	print(linha)
	print(texto)
	print(linha)

def exibir_opcoes():
	print('1 - Cadastrar Paciente')
	print('2 - Ver Estatisticas')
	print('3 - Buscar Paciente')
	print('4 - Listar Todos os Pacientes')
	print('5 - Sair')

def opcao_invalida():
	print('Opção Inválida! Digite um número de 1 a 5.')

def cadastrar_paciente():
	exibir_subtitulo('Cadastrando novo paciente')
	
	nome_paciente = input('Nome Completo: ')
	idade_paciente = input('Idade: ')
	telefone_paciente = input('Telefone: ')

	dados_do_paciente = {'nome': nome_paciente, 'idade': idade_paciente, 'telefone': telefone_paciente}
	lista_pacientes.append(dados_do_paciente)

	print(f'Paciente {nome_paciente} cadastrado com sucesso.')

def ver_estatisticas():
	pass

def buscar_paciente():
	pass

def listar_todos_pacientes():
	pass

def finalizar_programa():
	pass

def escolher_opcao():
	try:
		opcao_escolhida = int(input('Digite a opçao desejada: '))
		
		if opcao_escolhida == 1:
			cadastrar_paciente()
		if opcao_escolhida == 2:
			ver_estatisticas()
		if opcao_escolhida == 3:
			buscar_paciente()
		if opcao_escolhida == 1:
			listar_todos_pacientes()
		if opcao_escolhida == 1:
			finalizar_programa()

		else:
			opcao_invalida()

	except():
		opcao_invalida()
		
def main():
	os.system('cls')
	exibir_titulo()
	exibir_cabecalho_menu()
	exibir_opcoes()
	escolher_opcao()

if __name__ == '__main__':
	main()
