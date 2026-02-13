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

        int slow = n;
        int fast = n;

        while (true) {
        slow = square_digits(slow);
        fast = square_digits(square_digits(fast));

        if (slow == 1 || fast == 1) return true;
        if (slow == fast) return false; 
        } 
    }
}