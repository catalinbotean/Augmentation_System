from ui.ui import create_ui
from utils.files import get_images, read_images, create_directory
from utils.initialize import initialize_system
from utils.transformations import apply_augmentation

if __name__ == '__main__':
    processes_data = initialize_system()
    directory_path = create_ui()
    images_path = get_images(directory_path)
    images_data = read_images(images_path)
    new_directory = create_directory(directory_path)
    apply_augmentation(images_data, processes_data, new_directory)

