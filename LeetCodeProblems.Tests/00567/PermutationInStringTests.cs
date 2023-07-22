using LeetCodeProblems.Problems._00567;
using NUnit.Framework;

namespace LeetCodeProblems.Tests._00567;

public class PermutationInStringTests
{
    [SetUp]
    public void Setup()
    {
    }

    [Test]
    public void Test1()
    {
        var obj = new PermutationInString();
        Assert.AreEqual(true, obj.CheckInclusion("ab", "eidbaooo"));
    }

    [Test]
    public void Test2()
    {
        var obj = new PermutationInString();
        Assert.AreEqual(false, obj.CheckInclusion("ab", "eidboaoo"));
    }

    [Test]
    public void Test3()
    {
        var obj = new PermutationInString();
        Assert.AreEqual(true, obj.CheckInclusion("die", "eidboaoo"));
    }

    [Test]
    public void Test4()
    {
        var obj = new PermutationInString();
        Assert.AreEqual(false, obj.CheckInclusion("dieo", "eidboaoo"));
    }

    [Test]
    public void Test5()
    {
        var obj = new PermutationInString();
        Assert.AreEqual(true, obj.CheckInclusion("adc", "dcda"));
    }
}