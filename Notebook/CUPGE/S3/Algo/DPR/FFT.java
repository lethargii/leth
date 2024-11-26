import java.util.Arrays;

class Complexe{
    double x;
    double y;

    public Complexe(double x, double y){
        this.x = x;
        this.y = y;
    }

    public Complexe(){
        this.x = 0.;
        this.y = 0.;
    }

    static Complexe add(Complexe z1, Complexe z2){
        return new Complexe(z1.x+z2.x,z1.y+z2.y);
    }

    static Complexe sous(Complexe z1, Complexe z2){
        return new Complexe(z1.x-z2.x,z1.y-z2.y);
    }

    static Complexe mult(Complexe z1, Complexe z2){
        return new Complexe(z1.x*z2.x-z1.y*z2.y,z1.x*z2.y+z1.y*z2.x);
    }

    static Complexe omega(int k, int n){
        return new Complexe(Math.cos(2*k*Math.PI/n),Math.sin(2*k*Math.PI/n));
    }

    static Complexe[] dft_naive(Complexe[] poly){
       return null;
    }

    static Complexe[][] decompose(Complexe[] poly){
		return null;
    }

    static Complexe[] fft(Complexe[] poly){
        return null;
    }

    public String toString(){
        return ""+x+"+i."+y;
    }

    public static void main(String[] args) {
        Complexe[] p1 = new Complexe[4];
        p1[0] = new Complexe(1,0);
        p1[1] = new Complexe(2,0);
        p1[2] = new Complexe(2,0);
        p1[3] = new Complexe(1,0);
        Complexe[][] ps = decompose(p1);
        System.out.println(Arrays.toString(ps[0]));
        System.out.println(Arrays.toString(ps[1]));

        System.out.println(Arrays.toString(dft_naive(p1)));
        System.out.println(Arrays.toString(fft(p1)));

        Complexe c1 = omega(5, 8);
        Complexe c2 = omega(2, 8);
        Complexe c3 = omega(3, 8);
        System.out.println(c1);
        System.out.println(mult(c2, c3));
    }

}
