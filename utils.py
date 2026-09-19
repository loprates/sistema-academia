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
        return alunos[-1]['id'] + 1

def cadastrar_aluno():

        cpf = input("Digite o CPF do aluno: ").strip()

        while not valida_cpf(cpf):
            print("CPF inválido!")
            cpf = input("Digite o CPF novamente: ").strip()

        print("CPF válido!")

        aluno = {
            'id': criar_id(alunos),
            'nome': input("Digite o nome do aluno: ").strip(),
            'cpf': cpf,
            'atividade': int(input(
                "Digite a atividade: [0] Musculação | [1] Pilates | [2] Zumba: "
            )),
            'estado_matricula': int(input(
                "[0] Ativo | [1] Inativo: "
            )),
            'presença': 0
        }

        alunos.append(aluno)



        if aluno['atividade'] == 0:
            aluno['atividade'] = atividades[0]

        elif aluno['atividade'] == 1:
            aluno['atividade'] = atividades[1]

        elif aluno['atividade'] == 2:
            aluno['atividade'] = atividades[2]

        else:
            while True:
                atividade = int(input(
                    "Valor inválido, digite novamente: "
                     "[0] Musculação | [1] Pilates | [2] Zumba: "
                    ))

                if atividade > 2 or atividade < 0:
                        print("Digite um valor válido")

                else:
                    aluno['atividade'] = atividades[atividade]
                    salvar_dados()
                    break

        if aluno['estado_matricula'] == 0:
                aluno['estado_matricula'] = estados_matricula[0]

        elif aluno['estado_matricula'] == 1:
                aluno['estado_matricula'] = estados_matricula[1]

        else:
            while True:
                matricula = int(input(
                    "Valor inválido, digite novamente: "
                    "[0] Ativo | [1] Inativos: "
                ))

                if matricula > 1 or matricula < 0:
                    print("Digite um valor válido")

                else:
                    aluno['estado_matricula'] = estados_matricula[matricula]
                    salvar_dados()
                    break

def listar_alunos():
    for aluno in alunos:
        print(f"ID: {aluno['id']}\n Aluno: {aluno['nome']}\n CPF: {aluno['cpf']}\n Matricula: {aluno['estado_matricula']}\n Presença: {aluno['presença']}")

def atualizar_aluno():

        procura_aluno = str(input("Digite o nome do aluno: "))
        for aluno in alunos:

            if procura_aluno == aluno['nome']:

                print("""
                    1 - Registrar presença
                    2 - Atualizar matricula
                """)

                opcao = int(input("Digite a opção: "))

                if opcao == 1:

                    print("1 - Adicionar presença | 2 - Remover presença")
                    opcao1 = int(input())
                    if opcao1 == 1:
                        if not aluno['estado_matricula'] == "Ativo":

                            print("Não é possivel registrar presença de um aluno sem a matricula ativa")
                            break
                        aluno['presença'] += 1
                        salvar_dados()
                        break


                    elif opcao1 == 2:
                        aluno['presença'] -= 1

                        if aluno['presença'] < 0:
                            print("O aluno não pode ter uma presença negativa!")
                            aluno['presença'] = 0
                        
                        salvar_dados()
                        break    

                if opcao == 2:
                    if aluno['estado_matricula'] == 'Ativo':
                        aluno['estado_matricula'] = 'Inativo'
                        salvar_dados()
                        
                    elif aluno['estado_matricula'] == 'Inativo':
                        aluno['estado_matricula'] = 'Ativo'
                        salvar_dados()
                        
                    break

def excluir_aluno():
    remover_a = str(input("Digite o nome do aluno: "))
    for aluno in alunos:
        if remover_a == aluno['nome']:
            alunos.remove(aluno)