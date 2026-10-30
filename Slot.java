import java.util.Scanner;

public class Slot {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        char carParkingSlot[] = new char[20];
        
        for(int row = 0; row < carparkSlot.length; row++) {
            carParkSlot[row] = 'O';
        }
        
        String carParkingSystemMenu = """
              ========================================
                          MINI PARKING SYSTEM
              ========================================
                      Select[Option]
                1.  Parking Space
                2.  Available slot to park
                3.  leave a slot
                0.  Exit
              ========================================
                """;
        System.out.println(carParkingSystemMenu);
        
        boolean Space = false;
        while(true) {
        for(int row = 0; row < carParkingSlot.length; row++) {
            System.out.print(carparkSlot[row] + " ");
        }
        System.out.println();
      
        System.out.print("Enter your parking slot number: ");
        int parkingNumber = scanner.nextInt();
        
        int rowIndexa = parkingNumber - 1;

        if (rowIndexa >= 0 && rowIndexa < 20) {
                  
            if (carparkSlot[rowIndexa] == 'O') {
                carparkSlot[rowIndexa] = '1';
                
                for(int row = 0; row < parkingSlot.length; row++) {
                    System.out.print(carparkSlot[row] + " ");
                    }
                    System.out.println();
                    break;
            } 
                else {
                    System.out.println("Space has been occupied.");
                 
                }
        } 
            else { 
                System.out.println("Invalid space option. retry");
                Space = false;
            }
        }
    }
}
