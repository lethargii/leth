public class Client{
	private String nom;
	private Produit[] caddy;
	private int nbProduits;

	public Client(String nom){
		this.nom = nom;
		this.caddy = new Produit[100];
		this.nbProduits = 0;
	}

	public String getNom(){
		return nom;
	}

	private void ajouteProduit(Produit p){
		caddy[nbProduits] = p;
		nbProduits++;
	}

	public void choisitProduit(Magasin m, String nomProduit){
		ajouteProduit(m.choisitProduit(nomProduit));
	}

	public double calculerPrixTotal(){
		double prixTotal = 0;
		for(int i = 0; i < nbProduits; i++){
			prixTotal += caddy[i].getPrix();
		}
		return prixTotal;
	}

	public String toString(){
		String res = "Client (nom : " + getNom() + "), caddy :\n";
		for(int i = 0; i < nbProduits; i++){
			res += "	" + caddy[i] + "\n";
		}
		return res;
	}

	public static void main(String[] args){
		Magasin intermarche = new Magasin();
		Produit p1 = new Produit(1.95, "Pain");
		Produit p2 = new Produit(15, "Pates (cuisson non rapide)");
		Produit p3 = new Produit(45, "WD-40");
		Produit p4 = new Produit(200, "Babar");
		Produit p5 = new Produit(1000, "Stitch");
		intermarche.ajouteProduit(p1);
		intermarche.ajouteProduit(p2);
		intermarche.ajouteProduit(p3);
		intermarche.ajouteProduit(p4);
		intermarche.ajouteProduit(p5);
		Client c1 = new Client("Marc");
		c1.choisitProduit(intermarche, "WD-40");
		c1.choisitProduit(intermarche, "Pain");
		c1.choisitProduit(intermarche, "Stitch");
		System.out.println(intermarche);
		System.out.println(c1);
		System.out.println(c1.calculerPrixTotal());
	}
}
