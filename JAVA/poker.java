/**
 * HW
 */
public class HW {
    

public static void main(String[] args) {
    String[]r = {"Diamond","Clubs","Hearts","Spades"};
    String[]x = {"2","3","4","5","6","7","8","9","10","JACK","QUEEN","KING","ACE"};
    int[]num = new int[5];
    for(int i = 0; i < 5; i++){
        num[i] = (int)(Math.random()*51);
        for (int j = 0; j < i; j++){
            if(num[i]==num[j]){
                i--;
            }
        }
    }
    for (int i = 0; i < 5; i++)
       System.out.println(r[num[i]/13]+" 의 "+x[num[i]%13]);

}
}