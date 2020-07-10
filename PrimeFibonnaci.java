/**
 * @Author: hardcodecoder
 * @Date:   05:07:51 Monday 06 July 2020
 * @Last modified by:   hardcodecoder
 * @Last modified time: 05:05:00 Tuesday 07 July 2020
 */

 /**
  Given two numbers n1 and n2
  1. Find prime numbers between n1 and n2, then
  2. Make all possible unique combinations of numbers from the
     prime numbers list you found in step 1.
  3. From this new list, again find all prime numbers.
  4. Find smallest (a) and largest (b) number from the 2nd generated
     list, also count of this list.
  5. Consider smallest and largest number as the 1st and 2nd number to generate
     Fibonacci series respectively till the count (number of primes in the 2nd list).
  6. Print the last number of a Fibonacci series as an output
  */

import java.io.*;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.Scanner;

public class PrimeFibonnaci {

  /*
   * Checks if @param n is prime
   * return true if @param n is prime else false
   */
  public static boolean prime(int n) {
    for (int i = 2; i <= Math.floor(Math.sqrt(n)); i++) {
      if (n%i == 0) {
        return false;
      }
    }
    return true;
  }

  public static void main(String args[]) {
    System.out.println("Enter two prime numbers: ");
    Scanner sc = new Scanner(System.in);
    int n1 = sc.nextInt();
    int n2 = sc.nextInt();

    /*
    * Find all primes in the range n1 ~ n2
    */
    List<Integer> list1 = new ArrayList<>();
    for (int i = n1; i <= n2; i++) {
      if(prime(i)){
        list1.add(i);
      }
    }

    /*
    * Combine all prime numbers to form unique numbers
    */
    Set<Integer> unique = new HashSet<>();
    List<Integer> list2 = new ArrayList<>();
    for (int i = 0; i < list1.size(); i++) {
      String s1 = String.valueOf(list1.get(i));

      for (int j = 0; j < list1.size(); j++) {
        if (j == i)
          continue;
        String s2 = String.valueOf(list1.get(j));
        int value = Integer.parseInt(s1+s2);
        if (unique.add(value)) {
          list2.add(value);
        }
      }
    }
    unique.clear();

    /*
    * Find all primes from list2
    */
    List<Integer> list3 = new ArrayList<>();
    for (int i = 0; i < list2.size(); i++) {
      int c = list2.get(i);
      if (prime(c))
        list3.add(c);
    }

    /*
    * Find min and max from list3
    */
    long min = list3.get(0);
    long max = list3.get(0);
    for (int i = 1; i < list3.size(); i++) {
      int num = list3.get(i);
      if (num < min)
        min = num;
      if (num > max)
        max = num;
    }

    /*
    * Find fibonnaci upto list3.size() with min, max as first two numbers
    */
    int i = 2;
    long sum = 0;
    while(i < list3.size()) {
      sum = min + max;
      min = max;
      max = sum;
      i++;
    }
    System.out.println("Required fibonnaci number is: " + sum);
  }
}
