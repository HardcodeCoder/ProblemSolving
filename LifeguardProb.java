/**
 * @Author: hardcodecoder
 * @Date:   04:53:20 Wednesday 08 July 2020
 * @Last modified by:   hardcodecoder
 * @Last modified time: 08:29:37 Friday 10 July 2020
 */

 /**
  * Consider two coordinates A=(x1, y1) and B=(x2, y2) where A lies in the first quadrant
  * and B lies in the 4th quadrant. While moving in 1st quadrant the velocity is v*f, and that in the
  * 4th quadrant is v. Find a point in the x axix such that minimum time is required to reach point B
  * from point A
  */


import java.io.*;
import java.util.Scanner;

public class LifeguardProb {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int x1 = sc.nextInt();
    int y1 = sc.nextInt();
    int x2 = sc.nextInt();
    int y2 = sc.nextInt();
    float f = sc.nextFloat();

    int mx = x1 >= x2 ? x1 : x2;

    double[] time = new double[mx+1];

    for (int i = 0; i <= mx; i++) {
      double t = (Math.sqrt((Math.pow((x1 - i), 2) + (y1 * y1)))/f) + Math.sqrt(Math.pow((i-x2), 2) + y2*y2);
      time[i] = t;
    }

    double minIndex = 0;
    double min = time[0];
    for (int i = 1; i <= mx; i++) {
      if (time[i] < min) {
        minIndex = i;
        min = time[i];
      }
    }
    System.out.format("%.6f", minIndex);
  }
}
