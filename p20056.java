import java.util.ArrayList; // import the ArrayList class

import java.util.ArrayList;
import java.util.HashMap; // import the HashMap class

public class p20056{
  public static void main(String [] args){
    ArrayList<String> cars = new ArrayList<String>();
    cars.add("BMW");
    cars.add("ABCD");
    cars.add("BENZ");
    cars.add(0, "Hyundai");
    System.out.println(cars);

    HashMap<String, String> capitalCities = new HashMap<String, String>();
    capitalCities.put("England", "London");
    System.out.println(cars.get(0));


    System.out.println("Hello World");
    System.out.println("Hello World2");
  }
}
