# Depois de fazer em java, quis brincar com python.

class Veiculo:
    def __init__(self, categoria, marca, modelo, ano, preco):
        self.categoria = categoria
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco

    def exibir_informacoes(self):
        return f"{self.categoria}, {self.marca} {self.modelo}, Ano: {self.ano}, Preço: R${self.preco:.2f}"


class GerenciadorVeiculos:
    def __init__(self):
        self.veiculos = []

    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)

    def listar_veiculos(self):
        if not self.veiculos:
            print("Nenhum veículo cadastrado.")
            return
        for veiculo in self.veiculos:
            print(veiculo.exibir_informacoes())

    def buscar_por_categoria(self, categoria):
        resultados = [v for v in self.veiculos if v.categoria.lower()
                      == categoria.lower()]
        return resultados

    def buscar_por_marca(self, marca):
        resultados = [v for v in self.veiculos if v.marca.lower()
                      == marca.lower()]
        return resultados

    def remover_veiculo(self, modelo):
        for veiculo in self.veiculos:
            if veiculo.modelo.lower() == modelo.lower():
                self.veiculos.remove(veiculo)
                print(f"Veículo {modelo} removido com sucesso.")
                return
        print(f"Veículo {modelo} não encontrado.")


if __name__ == "__main__":
    gerenciador = GerenciadorVeiculos()

    while True:

        print("\n==== Cadastro de Veículos ====")
        print("1. Adicionar Veículo")
        print("2. Listar Veículos")
        print("3. Buscar Veículos por Categoria")
        print("4. Buscar Veículos por Marca")
        print("5. Remover Veículo")
        print("0. Sair")

        try:
            opcao = int(input("\nEscolha uma opção: "))
        except ValueError:
            print("Opção inválida! Por favor, digite um número.")
            continue

        if opcao == 0:
            print("Encerrando o programa...")
            break

        elif opcao == 1:
            try:
                add = int(input("\nQuantos veículos deseja adicionar? "))
                for i in range(add):
                    print(f"\n--- Cadastro do Veículo {i+1} ---")
                    try:
                        categoria = input("Categoria: ").strip().title()
                        marca = input("Marca: ").strip().title()
                        modelo = input("Modelo: ").strip().title()
                        ano = int(input("Ano: ").strip())
                        preco = float(input("Preço: ").strip())

                        veiculo = Veiculo(categoria, marca, modelo, ano, preco)
                        gerenciador.adicionar_veiculo(veiculo)
                        print("\n>>>> Veículo adicionado com sucesso! <<<<")
                    except ValueError:
                        print(
                            "Erro: Ano e Preço precisam ser números. Este veículo não foi salvo.")
            except ValueError:
                print("Erro: A quantidade precisa ser um número.")

        elif opcao == 2:
            print("\n===== Lista de Veículos: =====")
            gerenciador.listar_veiculos()
            voltar = input("\nDeseja voltar ao menu? (s/n)").strip().lower()
            if voltar == 's':
                continue
            else:
                print("Encerrando o programa...")
                break

        elif opcao == 3:
            categoria_busca = input(
                "\nDigite a categoria para buscar: ").strip().title()
            resultados = gerenciador.buscar_por_categoria(categoria_busca)
            print(f"\n=== Veículos da categoria {categoria_busca} ===")
            if not resultados:
                print("Nenhum veículo encontrado para esta categoria.")
            else:
                for veiculo in resultados:
                    print(veiculo.exibir_informacoes())
            voltar = input("\nDeseja voltar ao menu? (s/n)").strip().lower()
            if voltar == 's':
                continue
            else:
                print("Encerrando o programa...")
                break

        elif opcao == 4:
            marca_busca = input(
                "\nDigite a marca para buscar: ").strip().title()
            resultados = gerenciador.buscar_por_marca(marca_busca)
            print(f"\n=== Veículos da marca {marca_busca}: ===")
            for veiculo in resultados:
                print(veiculo.exibir_informacoes())
            voltar = input("\nDeseja voltar ao menu? (s/n)").strip().lower()
            if voltar == 's':
                continue
            else:
                print("Encerrando o programa...")
                break

        elif opcao == 5:
            modelo_remover = input(
                "\nDigite o modelo do veículo a ser removido: ").strip().title()
            gerenciador.remover_veiculo(modelo_remover)
            voltar = input("\nDeseja voltar ao menu? (s/n)").strip().lower()
            if voltar == 's':
                continue
            else:
                print("Encerrando o programa...")
                break
        else:
            print("Opção inválida. Tente novamente.")
            continue
