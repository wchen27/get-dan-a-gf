import java.util.*;

public class HackTJ2048{

   int[][] board = new int[4][4];
   int score = 4;
   int max = 2;

   public HackTJ2048(){
      for(int i = 0; i < 2; i++){
         int x = (int)(Math.random()*4);
         int y = (int)(Math.random()*4);
         if (checkSpot(x,y)) board[x][y] = 2;
         else i--;
      }
   }

   public boolean checkSpot(int x, int y){
      if (board[x][y] == 0) 
         return true;
      return false;
   }

   public void spawn(){
      while (true){
         int x = (int)(Math.random()*4);
         int y = (int)(Math.random()*4);
         if (checkSpot(x,y)){
            if (Math.random() > 0.1) board[x][y] = 2;
            else board[x][y] = 4;
            break;
         }
      }
   }
   
   public void updateNums(){
      int temp = 0;
      for (int[] in : board){
         for (int out : in){
            temp+=out;
            max = Math.max(max,out);
         }
      }
      score = Math.max(score,temp);
   }
   
   public boolean gameOver(int[][] arr) {
      for(int r=0;r<arr.length;r++) {
         for(int c=0;c<arr[r].length;c++){
            if(arr[r][c]==2048) 
               return true;
            if(c==0){
               if(arr[r][c+1]==arr[r][c]) 
                  return false;
            }
            else if(c==arr[r].length-1) {
               if(arr[r][c-1]==arr[r][c]) 
                  return false;
            }
            if(r==0){
               if(arr[r+1][c]==arr[r][c]) 
                  return false;
            }
            else if(r==arr.length-1){
               if(arr[r-1][c]==arr[r][c]) 
                  return false;
            }
            else{
               if(arr[r][c+1]==arr[r][c]) 
                  return false;
               if(arr[r][c-1]==arr[r][c]) 
                  return false;
               if(arr[r+1][c]==arr[r][c]) 
                  return false;
               if(arr[r-1][c]==arr[r][c]) 
                  return false;
            }
         }
      }
      return true;
   }
   
   public Object moveLeft(int[][] arr){
      int add = 0;
      for(int r=0;r<arr.length;r++) {
         for(int c=1;c<arr[r].length;c++) {
            if(arr[r][c-1]==0){
               arr[r][c-1]=arr[r][c];
               arr[r][c]=0;
            }
            if(arr[r][c]==arr[r][c-1]) {
               arr[r][c-1]*=2;
               arr[r][c]=0;
               add+=arr[r][c-1];
            }     
         }
      }
      return Object(board,add);
   }
   public Object moveRight(int[][] arr){
      for(int r=0;r<arr.length;r++) {
         int add = 0;
         for(int c=0;c<arr[r].length-1;c++) {
            if(arr[r][c+1]==0){
               arr[r][c+1]=arr[r][c];
               arr[r][c]=0;
            }
            if(arr[r][c]==arr[r][c+1]) {
               arr[r][c+1]*=2;
               arr[r][c]=0;
               add+=arr[r][c+1];
            }      
         }
      }
      return Object(board,add);
   }
   public Object moveUp(int[][] arr){
      int add = 0;
      for(int c=0;c<arr[0].length;c++) {
         for(int r=1;c<arr.length;r++) {
            if(arr[r-1][c]==0){
               arr[r-1][c]=arr[r][c];
               arr[r][c]=0;
            }
            if(arr[r-1][c]==arr[r][c]) {
               arr[r-1][c]*=2;
               arr[r][c]=0;
               add+=arr[r-1][c];
            }        
         }
      }
      return Object(board,add);
   }

   public Object moveDown(int[][] arr){
      int add = 0;
      for(int c=0;c<arr[0].length;c++) {
         for(int r=0;c<arr.length-1;r++) {
            if(arr[r+1][c]==0){
               arr[r+1][c]=arr[r][c];
               arr[r][c]=0;
            }
            if(arr[r+1][c]==arr[r][c]) {
               arr[r+1][c]*=2;
               arr[r][c]=0;
               add+=arr[r+1][c];
            }    
         }
      }
      return Object(board,add);
   }
   
   public void printGame(int[][] arr) {
      for(int r=0;r<arr.length;r++){
         for(int c=0;c<arr[r].length;c++) {
            if(arr[r][c]==0) System.out.print("- ");
            else System.out.print(arr[r][c]+ " ");
         }
         System.out.println("");
      }
   }
    
}