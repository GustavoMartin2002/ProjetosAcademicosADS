//Gustavo Lima Martin
//202109309587

#include <iostream>
#include <cstdlib>
using namespace std;

// Estrutura para armazenar o produto
struct Produto {
    string nome;
    float valorVenda;
    int estoque;
    Produto* proximo;
};

Produto *inserir_ordem(Produto* lista, string nomeProduto, float valorVenda) {
    Produto* novoProduto = new Produto;
    novoProduto->nome = nomeProduto;
    novoProduto->valorVenda = valorVenda;
    novoProduto->estoque = 0; 
    novoProduto->proximo = NULL;

    // Verifica se a lista est� vazia
    if (lista == NULL) {
        cout << "Produto " << nomeProduto << " inserido na lista" << endl;
        return novoProduto;
    } else {
        // Posiciona o ponteiro "p" na primeira posi��o da lista
        Produto* p = lista;

        // Testa se o primeiro elemento da lista � maior que o novo elemento
        if (p->nome > nomeProduto) {
            novoProduto->proximo = lista;
            cout << "Produto " << nomeProduto << " inserido na lista" << endl;
            return novoProduto;
        } else {
            // Testa se chegou ao fim da lista e se o elemento seguinte � menor que o novo elemento
            while (p->proximo != NULL && p->proximo->nome < nomeProduto) {
                p = p->proximo;
            }

            // Quando for localizada a posi��o correta para o novo elemento ser inserido,
            // faz o link do novo elemento apontar para o pr�ximo
            novoProduto->proximo = p->proximo;
            // Faz o link do elemento anterior apontar para o novo elemento
            p->proximo = novoProduto;
            cout << "Produto " << nomeProduto << " inserido na lista" << endl;
            return lista;
        }
    }
}

// Fun��o para encontrar um produto na lista
Produto* encontrarProduto(Produto* lista, string nome) {
    Produto* atual = lista;
    while (atual != NULL) {
        if (atual->nome == nome) {
            return atual;
        }
        atual = atual->proximo;
    }
    return NULL;
}

// Fun��o para comprar produtos
void comprarProduto(Produto* lista, string nome, int quantidade) {
    Produto* produto = encontrarProduto(lista, nome);
    if (produto != NULL) {
        produto->estoque += quantidade;
        cout << "Compra realizada com sucesso!" << endl;
    } else {
        cout << "Produto nao cadastrado!" << endl;
    }
}

// Fun��o para vender produtos
void venderProduto(Produto* lista, string nome, int quantidade) {
    Produto* produto = encontrarProduto(lista, nome);
    if (produto != NULL) {
        if (produto->estoque >= quantidade) {
            produto->estoque -= quantidade;
            float valorTotal = quantidade * produto->valorVenda;
            cout << "Venda realizada com sucesso! "<< "Valor total: R$" << valorTotal << endl;
        } else {
            cout << "Quantidade insuficiente em estoque!" << endl;
        }
    } else {
        cout << "Produto nao cadastrado!" << endl;
    }
    	
}

// Fun��o para exibir informa��es de um produto
void consultarProduto(Produto* lista, string nome) {
    Produto* produto = encontrarProduto(lista, nome);
    if (produto != NULL) {
        cout << "Produto: " << produto->nome << endl;
        cout << "Estoque disponivel: " << produto->estoque << endl;
        cout << "Valor total de vendas: R$" << produto->estoque * produto->valorVenda << endl;
    }
	else{
        cout << "Produto nao cadastrado!" << endl;
    }
}

// Fun��o para exibir a lista de produtos
void exibirProdutos(Produto* lista) {
    cout << "Lista de Produtos:" << endl;
    Produto* atual = lista;
    while (atual != NULL) {
        cout << "Nome: " << atual->nome << endl;
        cout << "Valor de Venda: " << atual->valorVenda << endl;
        cout << "Estoque: " << atual->estoque << endl;
        cout << endl;
        atual = atual->proximo;
    }
}

void liberarMemoria(Produto* lista) {
    Produto* atual = lista;
    while (atual != NULL) {
        Produto* proximo = atual->proximo;
        delete atual;
        atual = proximo;
    }
}
// Fun��o para exibir o menu
char exibirMenu() {
    char op;
    system("cls");
    cout << "1 - Cadastrar produto" << endl;
    cout << "2 - Comprar produto" << endl;
    cout << "3 - Vender produto" << endl;
    cout << "4 - Consultar produto" << endl;
    cout << "5 - Relacao de produtos" << endl;
    cout << "0 - Sair" << endl;
    cout << "Opcao: ";
    cin >> op;
    return op;
}

int main() {
	Produto* listaProdutos = NULL;
	char opcao = exibirMenu();
	string nome;
	string nomeProduto;
    float valorVenda;
    int quantidade;
    
    
    while (opcao != '0') {
        if (opcao == '1') {
            cout << "Nome do produto: ";
            cin >> nome;
            cout << "Valor de venda: ";
            cin >> valorVenda;
			listaProdutos = inserir_ordem(listaProdutos, nome, valorVenda);
            
        } else if (opcao == '2') {
            cout << "Nome do produto: ";
            cin >> nome;
            cout << "Quantidade a ser comprada: ";
            cin >> quantidade;
            comprarProduto(listaProdutos, nome, quantidade);
            
        } else if (opcao == '3') {
            cout << "Nome do produto: ";
            cin >> nome;
            cout << "Quantidade a ser vendida: ";
            cin >> quantidade;
            venderProduto(listaProdutos, nome, quantidade);
            
        } else if (opcao == '4') {
            cout << "Nome do produto: ";
            cin >> nome;
            consultarProduto(listaProdutos, nome);
            
        } else if (opcao == '5') {
        	exibirProdutos(listaProdutos);
        }

        system("pause");
        opcao = exibirMenu();
    }
	liberarMemoria(listaProdutos);
    return 0;
}