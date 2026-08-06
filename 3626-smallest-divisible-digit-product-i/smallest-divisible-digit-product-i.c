int smallestNumber(int n, int t) {
    for (; ; n++) {
        int temp = n;     
        int produto = 1;  

        while (temp > 0) {
            int last = temp % 10;
            produto *= last;
            temp /= 10;
        }
        if (produto % t == 0) {
            return n;
        }
    }
}