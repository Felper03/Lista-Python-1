# Dicionário global para armazenar os usuários
banco_usuarios = []

# Função para cadastrar um usuário
def cadastrar_usuario(campos_obrigatorios):
    usuario = {}
    for campo in campos_obrigatorios:
        valor = input(f'Digite o valor para o campo "{campo}": ')
        usuario[campo] = valor

    while True:
        mais_campos = input('Deseja adicionar mais campos (sim/sair)? ').lower()
        if mais_campos == 'sim':
            campo = input('Digite o nome do campo: ')
            valor = input(f'Digite o valor para o campo "{campo}": ')
            usuario[campo] = valor
        elif mais_campos == 'sair':
            break

    banco_usuarios.append(usuario)
    print('Usuário cadastrado com sucesso!')

# Função para imprimir usuários
def imprimir_usuarios(*args, **kwargs):
    opcao = input('1 - Imprimir todos\n2 - Filtrar por nomes\n3 - Filtrar por campos\n4 - Filtrar por nomes e campos\n0 - Sair\nEscolha uma opção: ')
    
    if opcao == '1':
        for usuario in banco_usuarios:
            print(usuario)
    elif opcao == '2':
        nomes = args
        for nome in nomes:
            for usuario in banco_usuarios:
                if nome in usuario.values():
                    print(usuario)
    elif opcao == '3':
        campo = input('Digite o campo de busca: ')
        valor = input(f'Digite o valor para o campo "{campo}": ')
        for usuario in banco_usuarios:
            if campo in usuario and usuario[campo] == valor:
                print(usuario)
    elif opcao == '4':
        nomes = args
        campos = kwargs.keys()
        for nome in nomes:
            for usuario in banco_usuarios:
                if nome in usuario.values():
                    for campo, valor in kwargs.items():
                        if campo in usuario and usuario[campo] == valor:
                            print(usuario)
    elif opcao == '0':
        return
    else:
        print('Opção inválida!')

# Função principal
def main():
    campos_obrigatorios = input('Digite os nomes dos campos obrigatórios separados por vírgula: ').split(',')
    
    while True:
        print('\nMenu:')
        print('1 - Cadastrar usuário')
        print('2 - Imprimir usuários')
        print('0 - Encerrar')
        
        opcao = input('Escolha uma opção: ')
        
        if opcao == '1':
            cadastrar_usuario(campos_obrigatorios)
        elif opcao == '2':
            imprimir_usuarios()
        elif opcao == '0':
            break
        else:
            print('Opção inválida! Tente novamente.')

if __name__ == "__main__":
    main()
