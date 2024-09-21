class Triangle{
	private Point p1;
	private Point p2;
	private Point p3;
	public Triangle(Point p1, Point p2, Point p3){
		this.p1 = p1;
		this.p2 = p2;
		this.p3 = p3;
	}
	public double perimetre(){
		return new Segment(p1, p2).longueur() + new Segment(p2, p3).longueur() + new Segment(p3, p1).longueur();
	}
	public void afficher(){
		System.out.println("Triangle[p1 : Point(" + this.p1.getX() + "," + this.p2.getY() + "), p2 : Point(" + this.p2.getX() + "," + this.p2.getY() + "), p3 : Point(" + this.p3.getX() + "," + this.p3.getY() + ")]");
	}
	public static void main(String[] args){
		Point p1 = new Point(2, 3);
		Point p2 = new Point(0, 0);
		Point p3 = new Point(-2, -3);
		Point p4 = new Point(4, 6);
		Point p5 = new Point(7, 14);
		Point p6 = new Point(21, 3);
		Triangle t1 = new Triangle(p1, p2, p3);
		Triangle t2 = new Triangle(p4, p5, p6);
		t1.afficher();
		t2.afficher();
	}
}
