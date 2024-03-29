class Solution {
public:
    int singleNumber(vector<int>& nums) {
        
        int n = nums.size();
        sort(nums.begin(), nums.end());

        for(int i = 0; i + 2 < n; i += 3)
        {
            if(nums[i] != nums[i + 1])
                return nums[i];
        }

        return nums[n - 1];
    }
};