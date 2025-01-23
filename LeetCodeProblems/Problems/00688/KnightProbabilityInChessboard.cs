namespace LeetCodeProblems.Problems._00688;

public class PermutationInString
{
    public bool CheckInclusion(string s1, string s2)
    {
        var chars = s1
            .GroupBy(c => c)
            .ToDictionary(x => x.Key, x => x.Count());

        for (var i = 0; i <= s2.Length - s1.Length; i++)
        {
            var window = s2.Substring(i, s1.Length);
            var windowChars = window
                .GroupBy(c => c)
                .ToDictionary(x => x.Key, x => x.Count());

            if (chars.Count == windowChars.Count &&
                chars.Keys.All(key => windowChars.ContainsKey(key) && chars[key] == windowChars[key]))
            {
                return true;
            }
        }

        return false;
    }
}