namespace LeetCodeProblems.Problems._00006;

public class ZigzagConversion
{
    public string Convert(string s, int numRows)
    {
        if (numRows == 1)
        {
            return s;
        }

        var positions = new Dictionary<(int, int), char>();
        var up = false;
        var x = 1;
        var y = 1;
        foreach (var c in s)
        {
            positions.Add((x, y), c);

            if (up)
            {
                x++;
                y--;
            }
            else
            {
                if (numRows > 1)
                {
                    y++;
                }
            }

            if (y == 1)
            {
                up = false;
            }

            if (y == numRows)
            {
                up = true;
            }
        }

        var result = "";
        for (var i = 1; i <= numRows; i++)
        {
            foreach (var pos in positions)
            {
                if (pos.Key.Item2 == i)
                {
                    result += pos.Value;
                }
            }
        }

        return result;
    }
}