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
        List<String> list1_k = new ArrayList<>(s_str.keySet());
        List<String> list2_k = new ArrayList<>(t_str.keySet());
        Collections.sort(list1_k);
        Collections.sort(list2_k);
        List<Integer> list1 = new ArrayList<>(s_str.values());
        List<Integer> list2 = new ArrayList<>(t_str.values());
        Collections.sort(list1);
        Collections.sort(list2);
        return (list1.equals(list2) && list1_k.equals(list2_k));

    }
}
