import matplotlib.pyplot as plt

def show_example(dataset, index):
    img, label = dataset[index][0], dataset[index][1]
    print('Label: ', dataset.classes[label], "("+str(label)+")")
    plt.imshow(img.permute(1, 2, 0))