import numpy as np 
import matplotlib.pyplot as plt
from typing import Tuple
import os
import multiprocessing as mlt
import itertools as it

def generate_pts(alpha: np.ndarray, speed: float) -> Tuple[np.ndarray, np.ndarray]: 
    x = np.cos(speed * alpha)
    y = np.sin(speed * alpha)

    return x, y


def plot_figures(
        nb_pts: int, 
        speed_0: int, 
        speed_1: int, 
        save: bool=False, 
        path_img: str="",
    ) -> None:
    # angle 
    print("yo")
    alpha = np.linspace(0, 2 * np.pi, nb_pts)

    # coords of the first points of the line
    pt0_x, pt0_y = generate_pts(alpha, speed_0)
    # coords of the second points of the line 
    pt1_x, pt1_y = generate_pts(alpha + np.pi, speed_1)

    theta = np.linspace(0, 2 * np.pi, 1000)
    cos_x = np.cos(theta)
    sin_y = np.sin(theta)

    pts_x = [(pt0_x[i], pt1_x[i]) for i in range(nb_pts)]
    pts_y = [(pt0_y[i], pt1_y[i]) for i in range(nb_pts)]

    plt.figure(figsize=(10, 10))
    plt.plot(cos_x, sin_y, color="black")

    for xs, ys in zip(pts_x, pts_y): 
        plt.plot(xs, ys, color="black")
    plt.xlim([-1.1, 1.1])
    plt.ylim([-1.1, 1.1])
    plt.axis("off")

    if save: 
        plt.savefig(path_img)
        plt.close()
    else:
        plt.show()

def hello(x, y): 
        print(x)

# create all the plots
if __name__ == "__main__": 
    speed_0 = 1 
    nb_pts = 150

    FOLDER_IMG = "img"

    # make a folder to store images 
    if os.path.isdir(FOLDER_IMG): 
        # remove all the old images from the folder storing the images 
        imgs = os.listdir(FOLDER_IMG)

        for img_name in imgs: 
            os.remove(f"{FOLDER_IMG}/{img_name}")

    else: 
        os.mkdir(FOLDER_IMG)


    # speed for the other extremity of the line
    arr_speed_1 = np.linspace(1, 10, 900)

    # names of the images to store on the disk 
    name_imgs = [f"{FOLDER_IMG}/img_{k}.jpg" for k in range(len(arr_speed_1))]

    # args for the multiprocessing 

    args = zip(
        it.repeat(nb_pts), 
        it.repeat(speed_0),
        arr_speed_1, 
        it.repeat(True), 
        name_imgs,
    )
    args = list(args)

    l_p = []
    for arg in args: 
        p = mlt.Process(target=plot_figures, args=arg)

        l_p.append(p)

    # make sure not too many processes get started at the same time 
    nb_processes = os.cpu_count() // 2 
    count = 0
    while count < len(l_p): 
        for p in l_p[count: count + nb_processes]: 
            p.start()

        for p in l_p[count: count + nb_processes]: 
            p.join()
        
        count += nb_processes

