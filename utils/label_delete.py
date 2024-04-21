import os 


def delete_unused_labels(
    root_dir: str,
    image_extension: str = '.jpg'
) -> None:
    """
    Удаляет разметку(.txt) если нет соответсвующей картинки (картинки предварительно удаляются в ручную)
    """

    img = root_dir + '/images'
    lbls = root_dir + '/labels'

    images = [i for i in os.walk(img)][0][2] # берем файлы в images
    img_filenames = []
    for im in images:
        if im.endswith(image_extension):
            img_filenames.append(im[:-4])
        else:
            continue

    labels = [i for i in os.walk(lbls)][0][2]

    for i in labels:
        if i[:-4] in img_filenames:
            continue
        else:
            os.remove(f'{lbls}/{i}')


delete_unused_labels('kmz_dataset_5cls_p1', 'train')
