// Concept d'objet
// Exercice 2
// 1.
public class conceptDObjet{
	public static void main(String[] args){
		new simulation().simulation();
	}
}
class Point{
	private double x;
	private double y;
	public double getX(){
		return this.x;
	}
	public double getY(){
		return this.y;
	}
	public void afficher(){
		System.out.println("Point(" + this.getX() + "," + this.getY() + ")");
	}
	public Point(double x, double y){
		this.x = x;
		this.y = y;
	}
}

// 2.
class Segment{
	private Point ext1;
	private Point ext2;
	public double longueur(){
		return Math.sqrt(Math.pow(ext2.getX()-ext1.getX(),2) + Math.pow(ext2.getY()-ext1.getY(),2));
	}
	public Segment(double x1, double y1, double x2, double y2){
		this.ext1 = new Point(x1, y1);
		this.ext2 = new Point(x2, y2);
	}
}

// 3.
class Triangle{
	private Point p1;
	private Point p2;
	private Point p3;
	public double perimetre(){
		return new Segment(p1.getX(), p1.getY(), p2.getX(), p2.getY()).longueur() + new Segment(p2.getX(), p2.getY(), p3.getX(), p3.getY()).longueur() + new Segment(p3.getX(), p3.getY(), p1.getX(), p1.getY()).longueur();
	}
	public void afficher(){
		System.out.println("Triangle[p1 : Point(" + this.p1.getX() + "," + this.p2.getY() + "), p2 : Point(" + this.p2.getX() + "," + this.p2.getY() + "), p3 : Point(" + this.p3.getX() + "," + this.p3.getY() + ")]");
	}
	public Triangle(double x1, double y1, double x2, double y2, double x3, double y3){
		this.p1 = new Point(x1, y1);
		this.p2 = new Point(x2, y2);
		this.p3 = new Point(x3, y3);
	}

}

// 4.
class simulation{
	public static void simulation(){
		Point p1 = new Point(2, 3);
		Point p2 = new Point(5, 1);
		Point p3 = new Point(-3, 7);
		Point p4 = new Point(4, 4);
		Point p5 = new Point(16, 0);
		Point p6 = new Point(3, 21);
		p1.afficher();
		p2.afficher();
		p3.afficher();
		p4.afficher();
		p5.afficher();
		p6.afficher();
		Triangle tri1 = new Triangle(p1.getX(), p1.getY(), p2.getX(), p2.getY(), p3.getX(), p3.getY());
		Triangle tri2 = new Triangle(p4.getX(), p4.getY(), p5.getX(), p5.getY(), p6.getX(), p6.getY());
		tri1.afficher();
		System.out.println(tri1.perimetre());
		tri2.afficher();
		System.out.println(tri2.perimetre());
	}
}
