public class Chaines{
	public static void main(String[] args){
		String s1 = "Coucou";
		String s2 = "Coucou";
		System.out.println("égalité s1 == s2 : " + (s1 == s2));
		String s3 = new String("Coucou");
		System.out.println("égalité s1 == s3 : " + (s1 == s3));
		System.out.println("égalité s1.equals(s2) : " + (s1.equals(s2)));
		System.out.println("égalité s1.equals(s3) : " + (s1.equals(s3)));
	}
}
