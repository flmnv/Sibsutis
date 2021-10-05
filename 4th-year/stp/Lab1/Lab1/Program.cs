using System;

namespace Lab1
{
    public class Lab
    {
        public Lab() { }

        public double FirstFunction(int[] ind, double[] v)
        {
            double result = 0;

            foreach (int index in ind)
            {
                if (index < v.Length && index >= 0)
                {
                    if (v[index] != 0)
                    {
                        if (result == 0)
                        {
                            result = v[index];
                        }
                        else
                        {
                            result *= v[index];
                        }
                    }
                }
            }

            return result;
        }

        public Tuple<int, int> SecondFunction(int[] array)
        {
            int index_min = 0;

            for (int i = 1; i < array.Length; i++)
            {
                if (array[i] < array[index_min])
                {
                    index_min = i;
                }
            }

            return Tuple.Create(array[index_min], index_min);
        }

        public double[] ThirdFunction(double[] array)
        {
            Array.Reverse(array);
            return array;
        }
    }


    class Program
    {
        static void Main(string[] args)
        {

        }
    }
}