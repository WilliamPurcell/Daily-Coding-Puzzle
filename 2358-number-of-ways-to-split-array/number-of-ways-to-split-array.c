int waysToSplitArray(int* nums, int numsSize) {
    double Lsum=0;
    double Rsum=0;
    int count = 0;
    for (int j = numsSize - 1; j > 0; j--) {
        Rsum += nums[j];
    }
    for (int i = 0; i < numsSize - 1; i++) {
        Lsum += nums[i];
        if (Lsum >= Rsum)
            count++;
        Rsum -= nums[i+1];
    }
    return count;
}