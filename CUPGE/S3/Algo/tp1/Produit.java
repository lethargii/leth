public class Produit{
	private double prix;
	private String nom;
	public Produit(double prix, String nom){
		this.prix = prix;
		this.nom = nom;
	}
	public double getPrix(){
		return this.prix;
	}
	public String getNom(){
		return this.nom;
	}
	public String toString(){
		return "Produit (nom : " + this.nom + ", prix : " + this.prix + ")";
	}
	public static void main(String[] args){
		Produit p1 = new Produit(3.45, "WD-40");
		System.out.println("p1 : " + p1);
	}
}
