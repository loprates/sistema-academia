from utils import salvar_dados, criar_id, cadastrar_aluno, listar_alunos, registrar_presenca, excluir_aluno


escolha = None

while escolha != 0:

    print("""
    1 - Cadastrar aluno
    2 - Listar alunos
    3 - Registrar presença
    4 - Excluir aluno
    0 - Sair
              """)

    while True:
        try:
            escolha = int(input('Digite uma opção: '))
            break

        except ValueError:
            print("Digite apenas números!")

    if escolha == 1:
        cadastrar_aluno()
        salvar_dados()
        continue

    elif escolha == 2:
        listar_alunos()
        salvar_dados()
        continue

    elif escolha == 3:
        registrar_presenca()
        salvar_dados()
        continue

    elif escolha == 4:
        excluir_aluno()
        salvar_dados()
        continue

    elif escolha == 0:
        salvar_dados()
        break