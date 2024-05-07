import convertapi
import config
import os

convertapi.api_secret = config.CONVERT_TOKEN

converted = None


class ConvertFilesApi:
    file_name = None
    convert_to = None

    def __init__(self, file, convert_to):
        self.set_data(file, convert_to)

    def set_data(self, file_name=None, convert_to=None):
        self.file_name = file_name
        self.convert_to = convert_to

    def convert(self):
        global converted
        file_name = self.file_name
        from_form = file_name.split('.')
        from_format = from_form[1]
        converted = self.file_name + f'-converted.{self.convert_to}'
        convertapi.convert(f'{self.convert_to}', {'File': f'./files_to_convert/{file_name}'},
                           from_format=from_format).save_files(f'./converted_files/{converted}')
        os.remove(f'./files_to_convert/{file_name}')
        return converted
