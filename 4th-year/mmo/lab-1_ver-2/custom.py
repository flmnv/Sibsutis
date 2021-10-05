import matplotlib.pyplot as pyplot
import pandas
import tkinter

# const
# class colors
colors = [
    "#CC0000", "#339933", "#336699", "#33CCCC", "#FFCC33",
    "#CCCC00", "#006666", "#FFFFFF", "#99CC33", "#6633FF"
]


class Point():
    def __init__(self, x: float, y: float, class_name: str) -> None:
        self.x = x
        self.y = y
        self.class_name = class_name


class Plane():
    def __init__(self) -> None:
        self.points: list = []


    def add_point(self, point: Point):
        self.points.append(point)


    def show(self, point_size: int = 1, scr_width: int = 600,
             scr_height: int = 600, frame_size: int = 10,
             bg_color: str = "#FFFFFF", frame_color: str = "#FFFFFF"):

        class_colors: dict = {}
        window = tkinter.Tk()

        window.title("mmo-lab-1")
        canvas = tkinter.Canvas(
            master=window,
            width=scr_width,
            height=scr_height,
            bg=frame_color
        )

        # create frame
        canvas.create_rectangle(
            1 + frame_size, 1 + frame_size,
            scr_width + 2 - frame_size, scr_height + 2 - frame_size,
            fill=bg_color,
            outline=bg_color
        )

        # dimensions for the window
        shift_x = min(self.points, key=lambda point: point.x).x
        shift_y = min(self.points, key=lambda point: point.y).y
        max_x = max(self.points, key=lambda point: point.x).x - shift_x
        max_y = max(self.points, key=lambda point: point.y).y - shift_y
        multiply_x = (scr_width - 2 * frame_size) / max_x
        multiply_y = (scr_height - 2 * frame_size) / max_y
        shift_x *= multiply_x
        shift_y *= multiply_y

        # unique class colors
        for point in self.points:
            if point.class_name not in class_colors:
                if len(class_colors) < len(colors):
                    class_colors[point.class_name] = len(class_colors)
                else:
                    print("Warning: Some classes are the same color (Exceeded the number of classes).")
                    break

        # draw points
        for point in self.points:
            if point.class_name in class_colors:
                canvas.create_oval(
                    frame_size + point.x * multiply_x - point_size - shift_x,
                    frame_size + (scr_height - point.y * multiply_y) - point_size - shift_y,
                    frame_size + point.x * multiply_x + point_size - shift_x,
                    frame_size + (scr_height - point.y * multiply_y) + point_size - shift_y,
                    fill=colors[class_colors[point.class_name]],
                    outline=colors[class_colors[point.class_name]]
                )
            else:
                canvas.create_oval(
                    point.x - 1, point.y - 1,
                    point.x + 1, point.y + 1,
                    fill="#00FF00",
                    outline="#00FF00"
                )

        # open window
        canvas.pack(expand=tkinter.YES, fill=tkinter.BOTH)
        window.mainloop()


def get_data(file_name: int, rand: float = None):
    data = pandas.read_csv(f"data/{file_name}.csv")

    if rand is not None and rand > 0:
        shuffle_data = data.sample(frac=rand)
        return shuffle_data
    else:
        return data
