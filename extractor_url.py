import re
import warnings

# Fictional value just to make the program functional

DOLLAR_TO_REAL_RATE = 5.5
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

        url_pattern = re.compile('(http(s)?://)?(www.)?(bytebank.com)(.br)?(/exchange)')
        match = url_pattern.match(self.url)

        if not match:
            raise ValueError('The URL is invalid')
            
    def get_url_base(self):
        question_index = self.url.find('?')
        if question_index == -1:
            return self.url
        else:
            url_base = self.url[:question_index]
            return url_base 

    def get_url_parameter(self):
        question_index = self.url.find('?')
        if question_index == -1:
            warnings.warn('The URL does not contain any parameters')
        else:
            url_parameter = self.url[question_index+1:]
            return url_parameter
        
    def get_parameter_value(self, parameter_name):
        parameter_index = self.get_url_parameter().find(parameter_name)
        value_index = parameter_index + len(parameter_name) + 1
        ampersand_index = self.get_url_parameter().find('&', value_index)
        if ampersand_index == -1:
            parameter_value = self.get_url_parameter()[value_index:]
        else:
            parameter_value = self.get_url_parameter()[value_index:ampersand_index]

        return parameter_value

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return f'{self.url} \nParameters: {self.get_url_parameter()} \nURL Base: {self.get_url_base()}'

    def __eq__(self, other):
        return self.url == other.url

# In the real world I would already have this with the user navigating the site, but for this simple example I'm asking for the user to provide it
# This is a template of what the url would look like, and what I'm manually inputing. It changes deppending on the user choice of input and output currency, and quantity.
# url = 'http://bytebank.com/exchange?inputCurrency=dollar&outputCurrency=real&quantity=100'
url = input('Input the URL of the conversion site: ')
extractor_url = ExtractorURL(url)

input_currency = extractor_url.get_parameter_value('inputCurrency')
output_currency = extractor_url.get_parameter_value('outputCurrency')
quantity = extractor_url.get_parameter_value('quantity')

if input_currency == 'dollar' and output_currency == 'real':
    converted_value = float(quantity) * DOLLAR_TO_REAL_RATE
    print(f'The value of ${quantity} dolars is equal to R${str(converted_value)} reais')
elif input_currency == 'real' and output_currency == 'dollar':
    converted_value = float(quantity) / DOLLAR_TO_REAL_RATE
    print(f'The value of R${quantity} reais is equal to ${str(converted_value)} dollars')
