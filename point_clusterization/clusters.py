import matplotlib.pyplot as plt
import random
import numpy as np
import csv


def distance(a, b):
    return np.linalg.norm(np.array(a) - np.array(b))


if __name__ == "__main__":

    data = open("points.txt", "r")
    x_point = []
    y_point = []
    xy = []
    for line in data:
        point = data.readline().replace("\n", "")
        point = point.strip().split("    ")
        x_point.append(int(point[0]))
        y_point.append(int(point[1]))
        xy.append((int(point[0]), int(point[1])))

    no_centroids = 15
    x_c = []
    y_c = []
    xy_c = []

    for i in range(no_centroids):
        x_centroid = random.randint(200000, 800000)
        x_c.append(x_centroid)
        y_centroid = random.randint(200000, 800000)
        y_c.append(y_centroid)
        xy_c.append((x_centroid, y_centroid))

    print(xy_c)

    colors = ["grey", "brown", "coral", "orange", "olive", "yellow", "cyan", "deepskyblue", "lime", "royalblue",
              "indigo", "magenta", "pink", "peru", "gold"]

    for iteration in range(15):

        # train_data = open("train.txt", "a+")
        # test_data = open("test.txt", "a+")
        best_distance = 1000000
        which_centroid = 0
        name = {}
        for i in range(no_centroids):
            name[i] = []

        for k in range(len(xy)):
            for l in range(len(xy_c)):
                new_distance = distance(xy[k], xy_c[l])
                if new_distance < best_distance:
                    best_distance = new_distance
                    which_centroid = l
            name[which_centroid].append(xy[k])
            for_training = [str(which_centroid), str(x_point[k]), str(y_point[k])]
            for_training = ', '.join(for_training)
            for_test = [str(x_point[k]), str(y_point[k])]
            for_test = ', '.join(for_test)
            # if iteration == 14:
            #     train_data.write(for_training)
            #     train_data.write(", ")
            #     test_data.write(for_test)
            #     test_data.write(", ")
            best_distance = 1000000
            which_centroid = 0

        for centroid in range(no_centroids):

            x_coords = []
            y_coords = []

            for elem1, elem2 in name[centroid]:
                x_coords.append(elem1)
                y_coords.append(elem2)

            plt.scatter(x_coords, y_coords, color=colors[centroid])
            plt.scatter(x_c[centroid], y_c[centroid], color="black", marker="v")

            x_c[centroid] = sum(x_coords) / (len(x_coords))
            y_c[centroid] = sum(y_coords) / (len(y_coords))
            xy_c[centroid] = (x_c[centroid], y_c[centroid])

            if iteration == 14:
                print(xy_c)

        plt.show()
