public class Point{
	private double x;
	private double y;
	public Point(double x, double y){
		this.x = x;
		this.y = y;
	}
	public double getX(){
		return this.x;
	}
	public double getY(){
		return this.y;
	}
	public void afficher(){
		System.out.println("Point(" + this.getX() + "," + this.getY() + ")");
	}
	public static void main(String[] args){
		Point point1 = new Point(2, 3);
		Point point2 = new Point(5, 7);
		Point point3 = new Point(-1, -2);
		point1.afficher();
		point2.afficher();
		point3.afficher();
	}
}
