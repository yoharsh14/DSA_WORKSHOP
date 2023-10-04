public class pattern9 {
    public static void main(String[] args) {
    int row = 5;
    int col = 5;
    int space = 0;
    for(int i=0;i<row;i++){
        for(int j=0;j<col-1;j++){
            System.out.print("*");
        }
     
        for(int j=0;j<space;j++)System.out.print(" ");

        for(int j=0;j<col-1;j++){
            System.out.print("*");
        }
       if(i<row-2) System.out.println("");
        space+=2;
        col--;
    }
    row = 5;
    col++;
    space-=2;
        for(int i=0;i<row;i++){
        for(int j=0;j<col-1;j++){
            System.out.print("*");
        }
     
        for(int j=0;j<space;j++)System.out.print(" ");

        for(int j=0;j<col-1;j++){
            System.out.print("*");
        }
        System.out.println();
        space-=2;
        col++;
    }
    }
}
