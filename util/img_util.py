import random
import os
import cv2
import skimage


def readImageFile(file_path):
    # read image as an 8-bit array
    img_bgr = cv2.imread(file_path)

    # convert to RGB
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    # convert the original image to grayscale
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

    return img_rgb, img_gray


def saveImageFile(img_rgb, file_path):
    try:
        # convert BGR
        img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

        # save the image
        success = cv2.imwrite(file_path, img_bgr)
        if not success:
            print(f"Failed to save the image to {file_path}")
        return success

    except Exception as e:
        print(f"Error saving the image: {e}")
        return False


class ImageDataLoader():

    def __init__(self, directory: str, shuffle: bool=False, transform: bool=False):
        """"Load directory of images."""
        self.__iter_num__ = 0
        self.directory: str = directory
        self.shuffle: bool = shuffle
        self.transform: bool = transform
        self.fileList: list = sorted(
            [os.path.join(directory, f) for f in os.listdir(directory) if
             f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))]
        )

        if not self.fileList:
            raise ValueError("Image files not found in the directory.")
        
        if self.shuffle:
            random.shuffle(self.fileList)

        self.num_files: int = len((self.fileList))
        
        self.image_data: list = list()

    def FetchData(self, denoising: bool=True, histogram_equalization: bool=True):
        """Loads image data into a list with each entry being [imgage_bgr_data, image_rgb_data, image_greyscale_data]"""
        self.image_data = [[raw_data := cv2.imread(img_path), cv2.cvtColor(raw_data, cv2.COLOR_BGR2RGB), cv2.cvtColor(raw_data, cv2.COLOR_BGR2GRAY)] for img_path in self.fileList]
        if denoising:
            for image in self.image_data:
                image[0] = cv2.fastNlMeansDenoisingColored(image[0],None,10,10,7,21)
                image[1] = cv2.fastNlMeansDenoisingColored(image[1],None,10,10,7,21)
                image[2] = cv2.fastNlMeansDenoising(image[2],None,10,7,21)
            pass
        if histogram_equalization:
            for image in self.image_data:
                image[2] = skimage.exposure.equalize_hist(image[2])
            pass
        return self.image_data
    
    def DisplayImage(self, index: int, color: str = "bgr"):
        """Displays an image from ImageDataLoader.image_data. Color must be "bgr", "rgb, or "gray".
        If data has not been fetched, runs ImageDataLoader.FetchData
        """

        if not self.image_data:
            self.FetchData()

        def showImg(image):
            cv2.imshow("Image", image)
            cv2.waitKey(0)
        
        translation_dict = {"bgr": 0, "rgb": 1, "gray": 2}
        try:
            image = self.image_data[index][translation_dict[color]]

        except KeyError as e:
            raise KeyError("Color data not found. Color variable must be 'bgr', 'rgb', or 'gray'.\n", e)
        
        showImg(image)

    def __len__(self):
        return self.num_files
    
    def __iter__(self):
        self.__iter_num__ = 0
        return self
    
    def __next__(self):
        if self.__iter_num__+1 > self.num_files:
            raise StopIteration
        else:
            self.__iter_num__ += 1
            return self.image_data[self.__iter_num__-1]
