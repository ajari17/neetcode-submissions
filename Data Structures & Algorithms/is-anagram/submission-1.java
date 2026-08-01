class Solution 
{
    public boolean isAnagram(String s, String t) 
    {
        if(s.length() != t.length())
        {
            return false;
        }
        String[] one = new String[s.length()];
        String[] two = new String[s.length()];
        for(int i = 0; i < s.length(); i++)
        {
            one[i] = String.valueOf(s.charAt(i));
            two[i] = String.valueOf(t.charAt(i));
        }
        Arrays.sort(one);
        Arrays.sort(two);
        return Arrays.equals(one,two);
    }
}
