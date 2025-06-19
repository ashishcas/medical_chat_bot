class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        int n = nums.size();
        int start = 0 , end = 0;
        int sum = 0;
        int ans = 1;

        while(start <= end){
            sum += nums[end];
            if(sum == goal){
                ans++;
            }

            while(sum > goal ){
                sum -= nums[start];
                start++;
            }

            if(sum == goal){
                ans++;
            }
            end++;
        }
        return ans;
    }
};