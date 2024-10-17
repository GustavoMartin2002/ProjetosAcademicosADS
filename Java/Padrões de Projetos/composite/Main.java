package composite;

public class Main{
	
	public static void main(String[] args) {
		
		Refrigerante coca_cola = new Refrigerante("Coca Cola",8.5);
		FardoRefrigerante fardoCocaCola = new FardoRefrigerante();
		fardoCocaCola.add(coca_cola,6);
		
		System.out.println(
							"Produto: " + coca_cola.getNome() +
							"\n" + "Valor: " + coca_cola.getValor() +
							"\n" + "Fardo: " + fardoCocaCola.getValor()
		);
	}

}
