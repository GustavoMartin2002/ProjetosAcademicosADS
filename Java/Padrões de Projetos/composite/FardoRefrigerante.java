package composite;

import java.util.Arrays;
import java.util.ArrayList;
public class FardoRefrigerante implements Produto {
	private ArrayList<Produto> produtos = new ArrayList<>();
	public void add(Produto ...produtos) {
		this.produtos.addAll(Arrays.asList(produtos));
	}
	public void add(Produto produto, int quantidade) {
		for (int i = 0; i < quantidade; i++) {
			this.produtos.add(produto);
		}
	}
	public void remove(Produto produto) {
		produtos.remove(produto);
	}
	@Override
	public Double getValor() {
		Double soma = 0d;
		for (Produto produto : produtos) {
			soma += produto.getValor();
		}
		return soma;
	}
}

