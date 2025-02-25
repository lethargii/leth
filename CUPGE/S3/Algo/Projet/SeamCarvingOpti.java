import java.io.File;
import java.awt.image.BufferedImage;
import java.awt.Color;
import javax.imageio.ImageIO;

public class SeamCarvingOpti{
	// Attribut représentant l'image comme une matrice de pixels
	int[][] pixels;
	double[][] energies;

	// Constructeur initialisant pixels à partir du nom
	// d'un fichier représentant une image au format PNG
	public SeamCarvingOpti(String fileName){
		try{

			BufferedImage img=ImageIO.read(new File(fileName));
			int width = img.getWidth();
			int height = img.getHeight();
			pixels = new int[height][width];
			for (int i = 0; i < width; i++) {
				for (int j = 0; j < height; j++) {
					pixels[j][i] = img.getRGB(i, j) & 0xFF;
				}
			}
			energies = new double[height][width];

		}catch(Exception e){
			System.out.println("Erreur lors du chargement de \""+fileName+"\" : "+e);
		}
	}

	// Complexité : O(1)
	public double eij(int i, int j){
		double x = pixels[i][j-1]-pixels[i][j+1];
		double y = pixels[i-1][j]-pixels[i+1][j];
		return Math.sqrt(x*x + y*y);
	}

	// Complexité : O(n) avec n = pixels.length ou pixels[0].length
	public void maxEnergie(double valMax){
		for(int i = 0; i < energies.length; i++){
			energies[i][0] = valMax;
			energies[i][energies[0].length-1] = valMax;
		}
		for(int j = 1; j < energies[0].length-1; j++){
			energies[0][j] = valMax;
			energies[energies.length-1][j] = valMax;
		}
	}

	// Complexité : O(n*m) avec n = pixels.length et m = pixels[0].length
	public void energie(){
		double valMax = 0;
		for(int i = 1; i < pixels.length - 1; i++){
			for(int j = 1; j < pixels[0].length - 1; j++){
				energies[i][j] = eij(i, j);
				if(energies[i][j] > valMax){
					valMax = energies[i][j];
				}
			}
		}
		maxEnergie(valMax);
	}

	// Complexité : O(n) avec n = indexCout.length
	public void energie(int[] indexCout){
		double valMax = energies[0][0];
		energies[0] = supprimeCol(energies[0], indexCout[0]);
		energies[indexCout.length - 1] = supprimeCol(energies[indexCout.length - 1], indexCout[indexCout.length - 1]);
		for(int i = 1; i < indexCout.length - 1; i++){
			energies[i] = supprimeCol(energies[i], indexCout[i]);
			if(indexCout[i] < pixels[0].length - 1 && indexCout[i] > 0){
				energies[i][indexCout[i]] = eij(i, indexCout[i]);
			  if(energies[i][indexCout[i]] > valMax){
				  valMax = energies[i][indexCout[i]];
			  }
			}
			if(indexCout[i] > 1 && indexCout[i] < pixels[0].length - 1){
				energies[i][indexCout[i] - 1] = eij(i, indexCout[i] - 1);
			  if(energies[i][indexCout[i - 1]] > valMax){
				  valMax = energies[i][indexCout[i] - 1];
			  }
			}
		}
		if(valMax != energies[0][0]){
			maxEnergie(valMax);
		}
	}

	// Complexité : O(n) avec n = tab.length
	private int[] supprimeCol(int[] tab, int k){
		int[] res = new int[tab.length-1];
		for(int m = 0; m < k && m < res.length; m++){
			res[m] = tab[m];
		}
		for(int m = k; m < res.length; m++){
			res[m] = tab[m+1];
		}
		return res;
	}

	// Complexité : O(n) avec n = tab.length
	private double[] supprimeCol(double[] tab, int k){
		double[] res = new double[tab.length-1];
		for(int m = 0; m < k && m < res.length; m++){
			res[m] = tab[m];
		}
		for(int m = k+1; m < res.length; m++){
			res[m] = tab[m+1];
		}
		return res;
	}

	// Complexité : O(n*m) avec n = pixels.length et m = pixels[0].length
	private void suppressionNaive(){
		energie();
		int[] indexMin = new int[pixels.length];
		for(int i = 0; i < pixels.length; i++){
			for(int j = 0; j < pixels[0].length; j++){
				if(energies[i][j] < energies[i][indexMin[i]]){
					indexMin[i] = j;
				}
			}
			supprimePixel(i, indexMin[i]);
		}
	}

	// Complexité : O(n*m*k) avec n = pixels.length, m = pixels[0].length et k = k
	public void suppressionNaiveK(int k){
		for(int i = 0; i < k; i++){
			suppressionNaive();
		}
	}

	// Complexité : O(n*m) avec n = energies.length et m = energies[0].length
	public double[][] tableauCouture(double[][] energies){
		double[][] res = new double[energies.length][energies[0].length];
		for(int j = 0; j < res[0].length; j++){
			res[0][j] = energies[0][j];
		}
		for(int i = 1; i < res.length; i++){
			res[i][0] = energies[i][0] + Math.min(res[i-1][0], res[i-1][1]);
			res[i][res[0].length-1] = energies[i][res[0].length-1] + Math.min(res[i-1][res[0].length-2], res[i-1][res[0].length-1]);
			for(int j = 1; j < res[0].length-1; j++){
				res[i][j] = energies[i][j] + Math.min(res[i-1][j-1],Math.min(res[i-1][j],res[i-1][j+1]));
			}
		}
		return res;
	}

	// Complexité : O(n*m) avec n = energies.length et m = energies[0].length
	public int[][] tableauCouturePrec(double[][] energies){
		double[][] c = tableauCouture(energies);
		int[][] res = new int[energies.length][energies[0].length];
		for(int j = 0; j < res[0].length; j++){
			res[0][j] = -1;
		}
		for(int i = 1; i < res.length; i++){
			if(c[i-1][0] <= c[i-1][1]){
				res[i][0] = 0;
			}
			else{
				res[i][0] = 1;
			}
			if(c[i-1][res[0].length-1] <= c[i-1][res[0].length-2]){
				res[i][res[0].length-1] = res[0].length-1;
			}
			else{
				res[i][res[0].length-1] = res[0].length-2;
			}
			for(int j = 1; j < res[0].length-1; j++){
				if(c[i-1][j] <= c[i-1][j-1] && c[i-1][j] <= c[i-1][j+1]){
					res[i][j] = j;
				}
				else if(c[i-1][j-1] <= c[i-1][j] && c[i-1][j-1] <= c[i-1][j+1]){
					res[i][j] = j-1;
				}
				else{
					res[i][j] = j+1;
				}
			}
		}
		return res;
	}

	// Complexité : O(n) avec n = prec.length
	private int[] extractCout(int[][] prec, int j){
		int[] res = new int[prec.length];
		res[res.length-1] = j;
		for(int i = res.length-2; i >= 0; i--){
			res[i] = prec[i+1][res[i+1]];
		}
		return res;
	}

	// Complexité : O(n) avec n = pixels[i].length
	private void supprimePixel(int i, int j){
		pixels[i] = supprimeCol(pixels[i], j);
	}

	// Complexité : O(n*m) avec n = pixels.length et m = pixels[0].length
	private void supprimeCouture(int[] cout){
		for(int i = 0; i < pixels.length; i++){
			supprimePixel(i, cout[i]);
		}

	}

	// Complexité : O(n*m) avec n = pixels.length et m = pixels[0].length
	private void supprimeCoutureMin(){
		double[] tab = tableauCouture(energies)[pixels.length-1];
		int k = 0;
		for(int i = 1; i < tab.length; i++){
			if(tab[i] < tab[k]){
				k = i;
			}
		}
		int[] coutPrec = extractCout(tableauCouturePrec(energies), k);
		supprimeCouture(coutPrec);
		energie(coutPrec);
	}

	// Complexité : O(n*m*k) avec n = pixels.length, m = pixels[0].length et k = k
	public void seamCarving(int k){
		energie();
		for(int i = 0; i < k; i++){
			supprimeCoutureMin();
		}
	}

	// fonction permettant d'exporter une matrice de double vers un fichier
	// fileName représentant une image au format PNG.
	//
	// (utile pour exporter la matrice des énergies)
	//
	// Si le fichier est existant, il sera écrasé, sinon il sera créé.
	public static void exportToPng(String fileName, double[][] pixs){
		int[][] pixs2 = new int[pixs.length][pixs[0].length];
		double maxi = 0.;
		for(int i=0; i<pixs.length; i++) {
			for(int j=0; j<pixs[i].length; j++) {
				maxi = Math.max(maxi, pixs[i][j]);
			}
		}
		for(int i=0; i<pixs.length; i++) {
			for(int j=0; j<pixs[i].length; j++) {
				pixs2[i][j] = (int) (255*pixs[i][j]/maxi);
			}
		}
		exportToPng(fileName, pixs2);
	}

	// fonction permettant d'exporter une matrice de int vers un fichier
	// fileName représentant une image au format PNG.
	//
	// (utile pour exporter pixels)
	//
	// Si le fichier est existant, il sera écrasé, sinon il sera créé.
	public static void exportToPng(String fileName, int[][] pixs){
		try {
			BufferedImage image = new BufferedImage(pixs[0].length, pixs.length, BufferedImage.TYPE_INT_ARGB);
			for(int i=0; i<pixs.length; i++) {
				for(int j=0; j<pixs[i].length; j++) {
					int a = pixs[i][j];
					Color newColor = new Color(a,a,a);
					image.setRGB(j,i,newColor.getRGB());
				}
			}
			File output = new File(fileName);
			ImageIO.write(image, "PNG", output);
		}catch(Exception e){
			System.out.println("Erreur lors de l'export vers \""+fileName+"\" : "+e);
		}
	}

	// fonction privée auxiliaire pour toString
	private static String threeDigitInt(int n){
		if(n < 10){
			return "  "+n;
		}else if(n < 100){
			return " "+n;
		}else{
			return ""+n;
		}
	}

	// fonction permettant d'afficher la matrice pixels
	// de manière lisible
	public String toString(){
		String res = "[";
		for(int i = 0; i < pixels.length;i++){
			if(i != 0){
				res+=",\n ";
			}
			res+="[ "+threeDigitInt(pixels[i][0]);
			for(int j = 1; j < pixels[i].length;j++){
				res+=", "+threeDigitInt(pixels[i][j]);
			}
			res+=" ]";
		}
		return res+"]";
	}


	public static void main(String[] args){
		SeamCarvingOpti s = new SeamCarvingOpti("oiseau.png");
		s.seamCarving(240);
		exportToPng("test_3.png",s.pixels);
		// 6.
		// Le résultat est décevant car on supprime naïvement les pixels de moindre intesité ce qui peut créer des décalages dans l'image
		// 7.
		// c[0][j] = e[0][j]
		// 8.
		// c[i][j] = e[i][j] + min(c[i-1][j-1], c[i-1][j], c[i-1][j+1])
		// 15.
		// Il suffit de recalculer l'énergie des pixels autour de la couture.
	}
}
