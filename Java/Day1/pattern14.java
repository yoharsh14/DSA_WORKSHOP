public class pattern14 {
    public static void main(String[] args) {
        int row = 5;
        int col = 1;
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                char c = (char)('A'+j);
                System.out.print(c);
            }
            System.out.println();
            col++;
        }
    }
}
