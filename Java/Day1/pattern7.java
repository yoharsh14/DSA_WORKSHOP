public class pattern7 {
    public static void main(String[] args) {
        int space =5;
        int row = 5;
        int col = 1;
        for(int i=0;i<row;i++){
            for(int j=0;j<space;j++)System.out.print(" ");
            for(int j=0;j<col;j++)System.out.print("* ");
            System.out.println();
            col++;
            space--;
        }
    }
}
