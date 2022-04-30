class ExtractorURL():
    def __init__(self, url):
        self.url = self.sanitize_url(url)
        self.validate_url()
    
    def sanitize_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def validate_url(self):
        if not self.url:
            raise ValueError('The URL is empty')
            
    def get_url_base(self):
        question_index = self.url.find('?')
        url_base = self.url[:question_index]
        return url_base 

    def get_url_parameter(self):
        question_index = self.url.find('?')
        url_parameter = self.url[question_index+1:]
        return url_parameter
        
    def get_parameter_value(self, parameter_name):
        parameter_index = self.get_url_parameter().find(parameter_name)
        value_index = parameter_index + len(parameter_name) + 1
        ampersand_index = self.get_url_parameter().find('&', value_index)
        if ampersand_index == 1:
            parameter_value = self.get_url_parameter()[value_index:]
        else:
            parameter_value = self.get_url_parameter()[value_index:ampersand_index]

        return parameter_value