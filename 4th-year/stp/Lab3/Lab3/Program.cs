using System;

namespace Lab3
{
    public class Lab
    {
        /*
         * Функция получает целое числа a. Формирует и возвращает целое
         * число b из значений нечётных разрядов целого числа a, следующих в
         * обратном порядке. Например: a = 12345, b = 531.
         */
        public int FirstFunction(int a)
        {
            string strA = a.ToString();
            string result = "";

            for (int i = strA.Length - 1; i >= 0; i--)
                if ((i + 1) % 2 == 1)
                    result += strA[i];

            return Int32.Parse(result);
        }

        /*
         * Функция получает целое числа a. Находит и возвращает номер
         * разряда, в котором находится максимальное значение r среди чётных
         * разрядов целого числа a с чётным значением. Разряды числа,
         * пронумерованы справа налево, начиная с единицы. Например, а =
         * 62543, r = 4.
         */
        public int SecondFunction(int a)
        {
            string strA = a.ToString();
            int r = -1;

            for (int i = 1; i < strA.Length; i += 2)
            {
                char charA = (char)Char.GetNumericValue(strA[i]);

                if (charA % 2 == 0 && charA > r)
                    r = charA;
            }

            return r;
        }

        /*
         * Функция получает целое числа a. Возвращает число, полученное
         * циклическим сдвигом значений разрядов целого числа а на заданное
         * число позиций вправо. Например, сдвиг на две позиции:
         * Исходное число: 123456
         * Результат: 561234
         */
        public int ThirdFunction(int a, int offset)
        {
            string strA = a.ToString();
            string strResult = "";
            offset = offset % a.ToString().Length;

            for (int i = 0, numOffset; i < strA.Length; i++)
            {
                numOffset = (i + strA.Length - offset) % strA.Length;
                strResult += strA[numOffset];
            }

            return Int32.Parse(strResult);
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
