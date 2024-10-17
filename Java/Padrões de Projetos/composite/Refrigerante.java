package composite;

public class Refrigerante implements Produto {
	private String nome;
	private Double valor;
	public Refrigerante(String nome, Double valor) {
		this.nome = nome;
		this.valor = valor;
	}
	public String getNome() {
		return nome;
	}
	@Override
	public Double getValor() {
		return valor;
	}
}
