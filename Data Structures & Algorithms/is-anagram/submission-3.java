class Solution 
{
    public boolean isAnagram(String s, String t) 
    {
        if(s.length() != t.length())
        {
            return false;
        }
        HashMap<String, Integer> s_str = new HashMap<>();
        HashMap<String, Integer> t_str = new HashMap<>();
        for(int i = 0; i < s.length(); i++)
        {
            s_str.merge(String.valueOf(s.charAt(i)),1,Integer::sum);
            t_str.merge(String.valueOf(t.charAt(i)),1,Integer::sum);
        }
        return s_str.equals(t_str);

    }
}
