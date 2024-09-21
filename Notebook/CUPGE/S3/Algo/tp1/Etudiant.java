import java.util.HashMap;

public class Etudiant{
	private int numero;
	private String nom;
	private HashMap<Module,Double> notes;

	public Etudiant(int numero, String nom){
		this.numero = numero;
		this.nom = nom;
		notes = new HashMap<Module,Double>();
	}

	public String getNom(){
		return nom;
	}

	public int getNumero(){
		return numero;
	}

	public String toString(){
		String res = "Etudiant (nom : " + getNom() + ", numéro : " + getNumero() + "), notes :\n";
		for(Module module : notes.keySet()){
			res += "	" + module.getNom() + " : " + notes.get(module) + "\n";
		}
		return res;
	}

	public void ajouteNote(Module m, double note){
		notes.put(m, note);
	}

	public double getNote(Module m){
		return notes.get(m);
	}
}
