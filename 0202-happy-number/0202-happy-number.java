import java.util.HashSet;

class Solution {

    public int square_digits(int num) {
        int sum = 0;
        while (num > 0) {
            int digit = num % 10;
            sum += digit * digit;
            num /= 10;
        }
        return sum;
    }
    public boolean isHappy(int n) {

        HashSet<Integer> patterns = new HashSet<>();

        int next_num = n;

        while (!patterns.contains(next_num)) {
            patterns.add(next_num);
            next_num = square_digits(next_num);
            if (next_num == 1) return true;
        } 

        return false;
    }
}