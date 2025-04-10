public class Segment{
	private Point ext1;
	private Point ext2;
	public double longueur(){
		return Math.sqrt(Math.pow(ext2.getX()-ext1.getX(),2) + Math.pow(ext2.getY()-ext1.getY(),2));
	}
	public Segment(Point ext1, Point ext2){
		this.ext1 = ext1;
		this.ext2 = ext2;
	}
	public static void main(String[] args){
		Point p1 = new Point(2, 3);
		Point p2 = new Point(-1, 1);
		Point p3 = new Point(7, 4);
		Point p4 = new Point(-2, 3);
		Segment s1 = new Segment(p1, p2);
		Segment s2 = new Segment(p3, p4);
		System.out.println(s1.longueur());
		System.out.println(s2.longueur());
	}
}
