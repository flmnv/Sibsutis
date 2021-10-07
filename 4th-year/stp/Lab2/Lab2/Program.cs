using System;

namespace Lab2
{
    public class Lab
    {
        /*
         * Поиск минимума из трёх чисел.
         */
        public int FirstFunction(int num1, int num2, int num3)
        {
            int min = num1;

            if (num2 < min)
                min = num2;

            if (num3 < min)
                min = num3;

            return min;
        }

        /*
         * Функция получает двумерный массив вещественных переменных A.
         * Отыскивает и возвращает сумму значений компонентов массива, у
         * которых сумма значений индексов – чётная.
         */
        public double SecondFunction(double[,] array)
        {
            double sum = 0;

            for (int i = 0; i < array.GetLength(0); i++)
                for (int j = 0; j < array.GetLength(1); j++)
                    if ((i + j) % 2 == 0)
                        sum += array[i, j];

            return sum;
        }

        /*
         * Функция получает двумерный массив вещественных переменных A.
         * Отыскивает и возвращает максимальное значение компонентов массива,
         * лежащих на и ниже главной диагонали.
         */
        public double ThirdFunction(double[,] array)
        {
            double max = array[0, 0];

            for (int i = 1; i < array.GetLength(0); i++)
                for (int j = 0; j <= i && j < array.GetLength(1); j++)
                    if (max < array[i, j])
                        max = array[i, j];

            return max;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
    }
}
