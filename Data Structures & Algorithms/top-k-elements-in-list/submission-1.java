

class Solution 
{
    public int[] topKFrequent(int[] nums, int k) 
    {
        HashMap<Integer, Integer> occ = new HashMap<>();
        for(int i = 0; i < nums.length; i++)
        {
            if(occ.containsKey(nums[i]) == false)
            {
                occ.put(nums[i], 1);
            }
            else 
            {
                occ.put(nums[i], (occ.get(nums[i]) + 1));
            }
        }    
        return occ.entrySet().stream()
            // 1. Sort by frequency value in descending order
            .sorted((a, b) -> b.getValue().compareTo(a.getValue()))
            // 2. Take only the top k elements
            .limit(k)
            // 3. Extract the actual number (the key)
            .mapToInt(Map.Entry::getKey)
            // 4. Convert to an int[] array
            .toArray();

    }
}
