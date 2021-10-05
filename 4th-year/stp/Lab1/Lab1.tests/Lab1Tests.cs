using NUnit.Framework;
using System;

namespace Lab1.tests
{
    public class Lab1Tests
    {
        [SetUp]
        public void Setup()
        {
        }

        [Test]
        public void FirstFunction() // multiply
        {
            int[] ind = { 1, 2, 3, 4, -1, 7 };
            double[] v = { 0, 1.25, 5, 21 };
            double expected = 131.25;
            Lab lab = new Lab();

            double actual = lab.FirstFunction(ind, v);

            Assert.AreEqual(expected, actual);
        }

        [Test]
        public void SecondFunction() // minimum element and index
        {
            int[] array = { 6, 2, 0, 10, -10, 7 };
            Tuple<int, int> expected = Tuple.Create(-10, 4);
            Lab lab = new Lab();

            Tuple<int, int> actual = lab.SecondFunction(array);

            Assert.AreEqual(expected, actual);
        }

        [Test]
        public void ThirdFunction() // reverse massive
        {
            double[] array = { 0.001, 1, 2.35, 7.92, 0.087 };
            double[] expected = new double[] { 0.087, 7.92, 2.35, 1, 0.001 };
            Lab lab = new Lab();

            double[] actual = lab.ThirdFunction(array);

            Assert.AreEqual(expected, actual);
        }
    }
}