class Solution {

public:

    int findGCD(vector<int>& nums) 
        {
        int largest=0;
        int smallest=1000; 
        
        for(int i = 0; i < nums.size(); i++)
            {
            if(nums[i] > largest)
                largest = nums[i];
            if(nums[i] < smallest)
                smallest = nums[i];
            }
        if (smallest==largest)
            return largest;
        else
            return gcd(smallest,largest);
        }
    int gcd(int m, int n)
        {
        if(n==0)
            {
            return m;
            }
        else
            {
            int r=m%n;
            return gcd(n,r);
            }
        }
};

