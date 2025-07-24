import java.util.ArrayList;

public class Module{
	private String nom;
	private ArrayList<Etudiant> inscrits;

	public Module(String nom){
		this.nom = nom;
		inscrits = new ArrayList<Etudiant>();
	}

	public String getNom(){
		return nom;
	}

	public void inscrireEtudiant(Etudiant e){
		inscrits.add(e);
	}

	public String toString(){
		String res = "Module (nom : " + getNom() + "), inscrits :\n";
		for(Etudiant etudiant : inscrits){
			res += "	" + etudiant.getNumero() + "\n";
		}
		return res;
	}

	public static void main(String[] args){
		Etudiant e1 = new Etudiant(1, "Marc");
		Etudiant e2 = new Etudiant(2, "Alexandre");
		Etudiant e3 = new Etudiant(3, "Keita");
		Etudiant e4 = new Etudiant(4, "Lucien");
		Etudiant e5 = new Etudiant(5, "Julien");
		Etudiant e6 = new Etudiant(6, "Killian");
		Module m1 = new Module("Mathématiques");
		Module m2 = new Module("Anglais");
		m1.inscrireEtudiant(e1);
		m1.inscrireEtudiant(e2);
		m1.inscrireEtudiant(e3);
		m1.inscrireEtudiant(e4);
		m2.inscrireEtudiant(e4);
		m2.inscrireEtudiant(e5);
		m2.inscrireEtudiant(e6);
		e1.ajouteNote(m1, -20);
		e2.ajouteNote(m1, 13);
		e3.ajouteNote(m1, 18);
		e4.ajouteNote(m1, 21);
		e4.ajouteNote(m2, 21);
		e5.ajouteNote(m2, -800);
		e6.ajouteNote(m2, 16);
		System.out.println(e1);
		System.out.println(e2);
		System.out.println(e3);
		System.out.println(e4);
		System.out.println(e5);
		System.out.println(e6);
		System.out.println(m1);
		System.out.println(m2);
	}
}
