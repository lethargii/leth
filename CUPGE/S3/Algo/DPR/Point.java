import java.util.ArrayList;
import java.util.Random;

public class Point{
	double x;
	double y;
	Point(double x, double y){
		this.x = x;
		this.y = y;
	}
	double distanceTo(Point p){
		double dx = x-p.x;
		double dy = y-p.y;
		return Math.sqrt(dx*dx+dy*dy);
	}
	boolean lessXY(Point p){
		return x < p.x || (x == p.x && y < p.y);
	}
	boolean lessYX(Point p){
		return y < p.y || (y == p.y && x < p.x);
	}
	public Object clone(){
		return new Point(x,y);
	}

	public String toString(){
		return "("+(int)(10*x)*1.0/10+","+(int)(10*y)*1.0/10+")";
	}
	public static String tabtoString(Point[] tab){
		String res = "[";
		for(Point p : tab){
			res+=p+",";
		}
		return res+"]";
	}

	static Point[] pprocheNaive(ArrayList<Point> points){
		Point[] res = new Point[2];
		res[0] = points.get(0);
		res[1] = points.get(1);
		for(Point point1 : points){
			for(Point point2 : points){
				if(point1.distanceTo(point2) < res[0].distanceTo(res[1]) && point1 != point2){
					res[0] = point1;
					res[1] = point2;
				}
			}
		}
		return res;
	}

	static void quickSortX(ArrayList<Point> points, int i, int j){
		if(j>i+1){
			int pivot = i;
			for(int k=i+1;k<j;k++){
				if(points.get(k).lessXY(points.get(pivot))){
					Point tmp = points.get(pivot);
					points.set(pivot,points.get(k));
					points.set(k,points.get(pivot+1));
					points.set(pivot+1,tmp);
					pivot++;
				}
			}
			quickSortX(points, pivot+1, j);
			quickSortX(points, i, pivot);
		}
	}

	static void trierSelonX(ArrayList<Point> points){
		quickSortX(points, 0, points.size());
	}

	static void quickSortY(ArrayList<Point> points, int i, int j){
		if(j>i+1){
			int pivot = i;
			for(int k=i+1;k<j;k++){
				if(points.get(k).lessYX(points.get(pivot))){
					Point tmp = points.get(pivot);
					points.set(pivot,points.get(k));
					points.set(k,points.get(pivot+1));
					points.set(pivot+1,tmp);
					pivot++;
				}
			}
			quickSortY(points, pivot+1, j);
			quickSortY(points, i, pivot);
		}
	}

	static void trierSelonY(ArrayList<Point> points){
		quickSortY(points, 0, points.size());
	}

	static ArrayList<Point>[] diviser(ArrayList<Point> points, Point pivot){
		ArrayList<Point>[] res = new ArrayList[2];
		res[0] = new ArrayList<Point>();
		res[1] = new ArrayList<Point>();
		for(ArrayList<Point> el: res){
			el = new ArrayList<Point>();
		}
		for(Point point : points){
			if(pivot.lessXY(point)){
				res[0].add(point);
			}
			else{
				res[1].add(point);
			}
		}
		return res;
	}

	static ArrayList<Point> filtrer(ArrayList<Point> points, double x_mini, double x_maxi){
		ArrayList<Point> res = new ArrayList<Point>();
		for(Point point : points){
			if(point.x >= x_mini && point.x <= x_maxi){
				res.add(point);
			}
		}
		return res;
	}

	static Point[] pprocheDPR(ArrayList<Point> pointsX, ArrayList<Point> pointsY){
		if(pointsX.size() <= 3){
			return pprocheNaive(pointsX);
		}
		Point[] res = new Point[2];
		Point pivot = pointsX.get( (int) pointsX.size()/2-1);
		ArrayList<Point>[] pointsXGD = diviser(pointsX, pivot);
		ArrayList<Point>[] pointsYGD = diviser(pointsY, pivot);
		Point[] pointsG = pprocheDPR(pointsXGD[0], pointsYGD[0]);
		Point[] pointsD = pprocheDPR(pointsXGD[1], pointsYGD[1]);
		if(pointsG[0].distanceTo(pointsG[1]) < pointsD[0].distanceTo(pointsD[1])){
			res = pointsG;
		}
		else{
			res = pointsD;
		}
		double distMin = res[0].distanceTo(res[1]);
		ArrayList<Point> pointsM = filtrer(pointsY, pivot.x - distMin, pivot.x + distMin);
		for(int i = 0; i < pointsM.size()-1; i++){
			for(int j = i+1; j < Math.min(i+7, pointsM.size()-1); j++){
				double dist = pointsM.get(i).distanceTo(pointsM.get(j));
				if(dist < distMin){
					distMin = dist;
					res[0] = pointsM.get(i);
					res[1] = pointsM.get(j);
				}
			}
		}
		return res;
	}

	public static void main(String[] args) {
		int n = 100;
		System.out.println("Recherche des ppp parmi "+n+" points :");
		ArrayList<Point> points = new ArrayList<Point>();
		Random r = new Random();
		for(int i=0;i<n;i++){
			points.add(new Point(100*r.nextDouble(),100*r.nextDouble()));
		}
		long time = System.currentTimeMillis();
		Point[] ppp = pprocheNaive(points);
		System.out.println("Plus proches : "+ppp[0]+" et "+ppp[1]);
		System.out.println("Durée calcul : "+(1.*(System.currentTimeMillis()-time)/1000)+" secondes");

		ArrayList<Point> copyPoints = new ArrayList<Point>();
		copyPoints.addAll(points);

		trierSelonX(points);
		trierSelonY(copyPoints);

		time = System.currentTimeMillis();
		Point[] ppp2 = pprocheDPR(points,copyPoints);
		System.out.println("Plus proches : "+ppp2[0]+" et "+ppp2[1]);
		System.out.println("Durée calcul : "+(1.*(System.currentTimeMillis()-time)/1000)+" secondes");
	}
}
