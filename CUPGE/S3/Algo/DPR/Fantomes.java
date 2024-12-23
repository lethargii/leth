import java.util.Arrays;

class Fantomes{
    static boolean croise(int i, int j, int k, int l){
        return (j < k || l < i);
    }

    static boolean estAdmissible(int[] strat){
        // A compléter
        return false;
    }

    static boolean evalue(int[] c, int i, int j){
        // A compléter
        return false;
    }

    static boolean testStrategie(int[] strat){
        // A compléter
        return false;
    }

    static void cibles_aux(int[] p, int i, int j, int[] strat){
        // A compléter
    }

    static int[] cibles(int[] p){
        // A compléter
        return null;
    }

    public static void main(String[] args) {
        int[] strat1 = {1,0,5,4,3,2,7,6};
        int[] strat2 = {1,0,6,4,3,7,2,5};
        System.out.println(estAdmissible(strat1));
        System.out.println(estAdmissible(strat2));
        System.out.println(testStrategie(strat1));
        System.out.println(testStrategie(strat2));

        int[] p1 = {1,-1,1,1,-1,-1,-1,1};
        System.out.println(Arrays.toString(cibles(p1)));
    }
}
