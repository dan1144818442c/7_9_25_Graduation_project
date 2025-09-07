import config
from extracted_data.load_data import Loader
from kafka_ import kafka_producer

list_path = Loader.get_file_paths_in_list(config.PATH_TO_DIRECTORY)
pub = kafka_producer.Produce()

if __name__ == '__main__':
    # pub.publish_message("A" , "aa")
    for path in list_path:
        metadata_dic = Loader.get_metadata_of_file(path)
        print(metadata_dic)
        pub.publish_message(config.TOPIC_FOR_KAFKA , metadata_dic)
