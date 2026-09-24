import json
import re

def valida_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = re.sub(r'\D', '', cpf)
    
    # Verifica se tem 11 dígitos ou se todos são iguais
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
        
    # Cálculo do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10) % 11

    if digito1 == 10:
        digito1 = 0
        
    # Cálculo do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10) % 11

    if digito2 == 10:
        digito2 = 0
        
    # Compara os dígitos calculados com os informados
    return digito1 == int(cpf[9]) and digito2 == int(cpf[10])


atividades = ['Musculação', 'Pilates', 'Zumba']
estados_matricula = ['Ativo', 'Inativo']


try:
    with open("alunos.json", "r", encoding="utf-8") as arquivo:
        alunos = json.load(arquivo)

except FileNotFoundError:
    alunos = []


def salvar_dados():
    with open("alunos.json", "w", encoding="utf-8") as arquivo:
        json.dump(alunos, arquivo, ensure_ascii=False, indent=4)


def criar_id(alunos):
    if len(alunos) == 0:
        return 1
    else:
        maior_id = max(aluno['id'] for aluno in alunos)
        return maior_id + 1


def cadastrar_aluno():

    # Validação do CPF
    while True:
        cpf = input("Digite o CPF do aluno: ").strip()

        cpf = re.sub(r'\D', '', cpf)

        if not valida_cpf(cpf):
            print("CPF inválido!")
            continue

        cpf_cadastrado = False

        for aluno in alunos:
            if aluno['cpf'] == cpf:
                cpf_cadastrado = True
                break

        if cpf_cadastrado:
            print("CPF já cadastrado!")
            continue

        print("CPF válido!")
        break

    # Nome do aluno
    while True:
        nome = input("Digite o nome do aluno: ").strip()

        if nome == "":
            print("Digite um nome válido!")
        else:
            break

    # Escolha da atividade
    while True:
        try:
            atividade = int(input(
                "Digite a atividade: [0] Musculação | [1] Pilates | [2] Zumba: "
            ))

            if atividade < 0 or atividade > 2:
                print("Digite um valor válido!")
            else:
                break

        except ValueError:
            print("Digite apenas números!")

    # Escolha da matrícula
    while True:
        try:
            matricula = int(input(
                "[0] Ativo | [1] Inativo: "
            ))

            if matricula < 0 or matricula > 1:
                print("Digite um valor válido!")
            else:
                break

        except ValueError:
            print("Digite apenas números!")

    # Criação do aluno
    aluno = {
        'id': criar_id(alunos),
        'nome': nome,
        'cpf': cpf,
        'atividade': atividades[atividade],
        'estado_matricula': estados_matricula[matricula],
        'presença': 0
    }

    alunos.append(aluno)


def listar_alunos():
    for aluno in alunos:
        print(
            f"ID: {aluno['id']}\n"
            f" Aluno: {aluno['nome']}\n"
            f" CPF: {aluno['cpf']}\n"
            f" Atividade: {aluno['atividade']}\n"
            f" Matricula: {aluno['estado_matricula']}\n"
            f" Presença: {aluno['presença']}"
        )


def registrar_presenca():

    while True:
        listar_alunos()
        pass

        presenca_aluno = int(input('Digite o ID do aluno: '))
        for aluno in alunos:
            if aluno['id'] == presenca_aluno:
                print('\n [1] Adicionar presença | [2] Remover presença')
                opcao_r = int(input('Digite uma das opcões acima: '))
                if opcao_r == 1:
                    aluno['presença'] += 1
                    break

                elif opcao_r == 2:
                    aluno['presença'] -= 1
                    if aluno['presença'] < 0:
                        print('Um aluno não pode ter presença negativa!')
                        aluno['presença'] = 0
                    break

def atualizar_matricular():
    listar_alunos()
    pass

    matricula_aluno = 

def excluir_aluno():

    while True:
        try:
            remover_a = int(input("Digite o id do aluno: "))
            break

        except ValueError:
            print("Digite apenas números!")

    for aluno in alunos:
        if remover_a == aluno['id']:
            print(
                f"\nID: {aluno['id']}"
                f"\nNome: {aluno['nome']}"
                f"\nCPF: {aluno['cpf']}"
            )

            alunos.remove(aluno)
            return

    print("Aluno não encontrado!")