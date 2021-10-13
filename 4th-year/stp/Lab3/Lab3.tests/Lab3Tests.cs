using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Lab3.tests
{
    [TestClass]
    public class Lab3Tests
    {
        [TestMethod]
        public void FirstFunctionTest1()
        {
            Lab lab = new Lab();
            int a = 1;
            int expected = 1;
            int actual = lab.FirstFunction(a);

            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void FirstFunctionTest2()
        {
            Lab lab = new Lab();
            int a = 12345;
            int expected = 531;
            int actual = lab.FirstFunction(a);

            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void SecondFunctionTest1()
        {
            Lab lab = new Lab();
            int a = 1;
            int expected = -1;
            int actual = lab.SecondFunction(a);

            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void SecondFunctionTest2()
        {
            Lab lab = new Lab();
            int a = 2;
            int expected = -1;
            int actual = lab.SecondFunction(a);

            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void SecondFunctionTest3()
        {
            Lab lab = new Lab();
            int a = 11;
            int expected = -1;
            int actual = lab.SecondFunction(a);

            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void SecondFunctionTest4()
        {
            Lab lab = new Lab();
            int a = 12;
            int expected = 2;
            int actual = lab.SecondFunction(a);

            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void SecondFunctionTest5()
        {
            Lab lab = new Lab();
            int a = 62543;
            int expected = 4;
            int actual = lab.SecondFunction(a);

            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void ThirdFunctionTest1()
        {
            Lab lab = new Lab();
            int a = 123456;
            int offset = 2;
            int expected = 561234;
            int actual = lab.ThirdFunction(a, offset);

            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void ThirdFunctionTest2()
        {
            Lab lab = new Lab();
            int a = 123456;
            int offset = 0;
            int expected = 123456;
            int actual = lab.ThirdFunction(a, offset);

            Assert.AreEqual(expected, actual);
        }
    }
}