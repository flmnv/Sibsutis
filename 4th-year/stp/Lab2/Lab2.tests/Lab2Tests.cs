using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Lab2.tests
{
    [TestClass]
    public class Lab2Tests
    {
        [TestMethod]
        public void FirstFunctionTest1()
        {
            Lab lab = new Lab();

            int num1 = 2;
            int num2 = 0;
            int num3 = 5;
            int expected = 0;

            int actual = lab.FirstFunction(num1, num2, num3);

            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void FirstFunctionTest2()
        {
            Lab lab = new Lab();

            int num1 = 7;
            int num2 = 14;
            int num3 = 3;
            int expected = 3;

            int actual = lab.FirstFunction(num1, num2, num3);

            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void SecondFunctionTest1()
        {
            Lab lab = new Lab();

            double[,] array = {
                { 10, 7 }
            };
            int expected = 10;

            double actual = lab.SecondFunction(array);

            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void SecondFunctionTest2()
        {
            Lab lab = new Lab();

            double[,] array = {
                { -2, 11, 3 },
                { 17, 8, -9 },
                { 6, 7, -1 }
            };
            int expected = 14;

            double actual = lab.SecondFunction(array);

            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void ThirdFunctionTest1()
        {
            Lab lab = new Lab();

            double[,] array = { { 7 } };
            int expected = 7;

            double actual = lab.ThirdFunction(array);

            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void ThirdFunctionTest2()
        {
            Lab lab = new Lab();

            double[,] array = {
                {-4,-3, -2 },
                {-1, 0, 1 },
                {2, 3, 4 }
            };
            int expected = 4;

            double actual = lab.ThirdFunction(array);

            Assert.AreEqual(expected, actual);
        }
    }
}
