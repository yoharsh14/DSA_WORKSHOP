class pattern2{
    public static void main(String[] args){
        int row = 5;
        for(int i=0;i<row;i++){
            int col = i+1;
            for(int j=0;j<col;j++){
                System.out.print("*");
            }
            System.out.println();
        }
    }
}