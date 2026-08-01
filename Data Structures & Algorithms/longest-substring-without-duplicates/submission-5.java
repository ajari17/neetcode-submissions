class Solution 
{
    public int lengthOfLongestSubstring(String s) 
    {
        Set<Character> seen = new HashSet<>();
        int max = 0;
        int i = 0;
        for(int j = 0; j < s.length();j++)
        {
            while (seen.contains(s.charAt(j)))
            {
                seen.remove(s.charAt(i));
                i++;
            }
            seen.add(s.charAt(j));
            max = Math.max(max, j-i+1);

        }
        return max;
    }
}
