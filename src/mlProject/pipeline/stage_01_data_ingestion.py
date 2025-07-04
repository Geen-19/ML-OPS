from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_ingestion import DataIngestion

from mlProject import logger


STAGE_NAME = "Data Ingestion Stage"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
        
if __name__ == "__main__":
    try:
        pipeline = DataIngestionPipeline()
        pipeline.main()
    except Exception as e:
        logger.exception(e)
        raise e