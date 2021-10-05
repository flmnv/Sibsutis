# Вариант 16
# Nв = 2, Nя = 2, Nф = 4
# Метод парзеновского окна с фиксированным h
# T – треугольное
# Файл 4

import numpy
import pandas


def distance(x1, y1, x2, y2):
    return numpy.sqrt(numpy.power((x1 - x2), 2) + numpy.power((y1 - y2), 2))


def core(r: float, type: int):
    if numpy.fabs(r) > 1:
        return 0
    elif type == 0:
        return 1 - numpy.fabs(r)
        


def algorithm(test_data: pandas.DataFrame, train_data: pandas.DataFrame,
              type_core: int, h: float):
    """
    `train_data`: data for training

    `test_data`: data, the result of which needs to be found

    `h`: window width

    `type_core`:
    - Triangular core: 0
    """
    result_data: dict = {
        "MrotInHour": [],
        "Salary": [],
        "Class": []
    }

    print(
        f"Test data count: {len(test_data)}"
        f"\nTrain data count: {len(train_data)}"
    )

    for i in test_data.index:
        test_data.at[i, "Class"] = -2

    print(test_data)

    for i in test_data.index:
        weight_classes: list = []

        for j in range(len(train_data)):
            j_distance = distance(
                    x1=test_data["MrotInHour"][i],
                    y1=test_data["Salary"][i]/1000,
                    x2=train_data["MrotInHour"][j],
                    y2=train_data["Salary"][j]/1000
                )

            weight_classes.append([
                core(j_distance / h, 0),
                train_data["Class"][j]
            ])

        max_weight = max(weight_classes, key=lambda weight_class: weight_class[0])
        if max_weight[0] != 0:
            test_data.at[i, "Class"] = max_weight[1]
        else:
            test_data.at[i, "Class"] = -1

    print(test_data)


def get_data(rand: float = None):
    data = pandas.read_csv("data/data4.csv")

    if rand is not None and rand > 0:
        shuffle_data = data.sample(frac=rand)
        return shuffle_data
    else:
        return data


def main():
    data = get_data()
    test_data_count = round(len(data)*1/3)
    train_data_count = round(len(data)*2/3)

    print(f"Elements count: {len(data)}")

    algorithm(
        test_data=data.tail(10),
        train_data=data.head(train_data_count),
        type_core=0,
        h=0.5
    )
    

if __name__ == "__main__":
    main()
