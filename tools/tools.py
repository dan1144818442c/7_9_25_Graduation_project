import config

class Tools:
    @staticmethod
    def get_unice_id(dic_):
        return dic_[config.UNIQUE_FIELD_INDENTIFIER_IN_JSON]