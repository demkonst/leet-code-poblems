using LeetCodeProblems.Problems._6;
using NUnit.Framework;

namespace LeetCodeProblems.Tests._6;

public class ZigzagConversionTests
{
    [SetUp]
    public void Setup()
    {
    }

    [Test]
    public void Test1()
    {
        var obj = new ZigzagConversion();
        Assert.AreEqual("PAHNAPLSIIGYIR", obj.Convert("PAYPALISHIRING", 3));
    }

    [Test]
    public void Test2()
    {
        var obj = new ZigzagConversion();
        Assert.AreEqual("PINALSIGYAHRPI", obj.Convert("PAYPALISHIRING", 4));
    }

    [Test]
    public void Test3()
    {
        var obj = new ZigzagConversion();
        Assert.AreEqual("A", obj.Convert("A", 1));
    }

    [Test]
    public void Test4()
    {
        var obj = new ZigzagConversion();
        Assert.AreEqual("AB", obj.Convert("AB", 1));
    }
}