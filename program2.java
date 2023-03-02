#reverse a string using recursion in java
public class reverseString {
public static String reverse(String str) {
        // base case
        if (str.isEmpty()) {
            return str;
        }
        // recursive case
        else {
            return reverse(str.substring(1)) + str.charAt(0);
        }
    }
    public static void main(String[] args) {
        String str = "IARE";
        System.out.println(reverse(str)); // prints "dlrow olleh"
    }
}
