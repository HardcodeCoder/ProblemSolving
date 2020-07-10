/**
 * @Author: hardcodecoder
 * @Date:   04:58:54 Monday 06 July 2020
 * @Last modified by:   hardcodecoder
 * @Last modified time: 04:54:56 Tuesday 07 July 2020
 */

 /**
  * Find the minimum number of denominations for any arbitrary max price n for an item.
  *
  * Example 1: Lets suppose the maximum price of an item is 5$ then we can make coins
  * of {$1, $2, $3} to purchase any item ranging from $1 till $5.
  * So minimum number of denominations of coins required is 3.
  *
  * Example 2: Lets suppose the maximum price of an item is 10$ then we can make coins
  * of {$1, $2, $3, $4} or {$1, $2, $3, $5} to purchase any item ranging from $1 till $5.
  * So minimum number of denominations of coins required is 4.
  */


import java.io.*;
import java.util.Scanner;

public class PhilalandCoin {

  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    // Takes in number of test cases
    int n = sc.nextInt();

    // Initialize array to store the outputs
    int[] outputs = new int[n];

    for (int i = 0; i < n; i++) {
      // Reads input
      int num = sc.nextInt();

      // Stores the minimum number of denomination
      int count = 0;

      // Find the min denomination for input num
      while (num > 0) {
        count ++;
        num >>=1;
      }

      // Store the output
      outputs[i] = count;
    }

    // print the result
    for (int i = 0; i < n; i++) {
      System.out.println(outputs[i]);
    }
  }
}
