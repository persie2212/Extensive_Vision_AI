import seaborn as sns
import matplotlib.pyplot as plt
import torch
import numpy as np
sns.set()
# plt.style.use("dark_background")


def plot_metrics(train_metric, test_metric):
    (train_acc, train_losses) = train_metric
    (test_acc, test_losses) = test_metric

    fig, axs = plt.subplots(2, 2, figsize=(15, 10))
    axs[0, 0].plot(train_losses)
    axs[0, 0].set_title("Training Loss", color='r')
    axs[1, 0].plot(train_acc[500:])
    axs[1, 0].set_title("Training Accuracy", color='r')
    axs[0, 1].plot(test_losses)
    axs[0, 1].set_title("Test Loss", color='r')
    axs[1, 1].plot(test_acc)
    axs[1, 1].set_title("Test Accuracy", color='r')

# Function to plot misclassified images


def plot_misclassified(model, test_loader, device):
    # Visualize the misclassified images
    model.eval()

    figure = plt.figure(figsize=(10, 10))
    num_of_images = 25
    index = 1

    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(
                device), target.to(device)
            output = model(data)
            pred = output.argmax(dim=1, keepdim=True)
            act = target.view_as(pred)
            # since most of the bool vec is true (good problem to have) and switch (flip) the true to false and vice versa
            bool_vec = ~pred.eq(act)

            # now extract the index number from the tensor which has 'true'
            idx = list(
                np.where(bool_vec.cpu().numpy())[0])

            if idx:  # if not a blank list
                idx_list = idx
                # print(data[idx_list[0]].shape)
                if index < num_of_images+1:

                    plt.subplot(5, 5, index)
                    plt.axis('off')
                    titl = 'act/pred : ' + \
                        str(target[idx[0]].cpu().item(
                        )) + '/' + str(pred[idx[0]].cpu().item())
                    # prints the 1st index of each batch.
                    plt.imshow(
                        data[idx[0]].cpu().numpy().squeeze())
                    plt.title(titl)
                    index += 1


def multi_plots_loss(metric_values):
    # plot Loss for all models
    plt.figure(figsize=(8, 6))
    plt.title('validation Loss')
    plt.xlabel('epochs')
    plt.ylabel('Loss')
    for idx, exp_name in enumerate(metric_values.keys()):
        train_metric, test_metric = metric_values[exp_name]
        train_acc, train_loss = train_metric
        test_acc, test_loss = test_metric
        plt.plot(test_loss, label='{}'.format(exp_name))

    plt.legend()
    plt.show()


def multi_plots_acc(metric_values):
    # plot Loss for all models
    plt.figure(figsize=(8, 6))
    plt.title('validation Accuracy')
    plt.xlabel('epochs')
    plt.ylabel('accuracy')
    for idx, exp_name in enumerate(metric_values.keys()):
        train_metric, test_metric = metric_values[exp_name]
        train_acc, train_loss = train_metric
        test_acc, test_loss = test_metric
        plt.plot(test_acc, label='{}'.format(exp_name))

    plt.legend()
    plt.show()
