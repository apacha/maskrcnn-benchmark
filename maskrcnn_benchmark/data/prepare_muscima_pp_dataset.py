from omrdatasettools.converters.ImageColorInverter import ImageColorInverter
from omrdatasettools.downloaders.MuscimaPlusPlusDatasetDownloader import MuscimaPlusPlusDatasetDownloader

if __name__ == "__main__":
    destination_directory = "../../datasets/muscima_pp"

    dataset_downloader = MuscimaPlusPlusDatasetDownloader()
    dataset_downloader.download_and_extract_dataset(destination_directory)
    dataset_downloader.download_and_extract_measure_annotations(destination_directory)

    image_color_inverter = ImageColorInverter()
    image_color_inverter.invert_images(destination_directory, "*.png")
