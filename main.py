url = 'http://bytebank.com/exchange?inputCurrency=real&outputCurrency=dollar&quantity=100'

# Separate base and parameters
question_index = url.find('?')
url_base = url[:question_index]
url_parameters = url[question_index+1:]

parameter_name = 'outputCurrency'
parameter_index = url_parameters.find(parameter_name)
value_index = parameter_index + len(parameter_name) + 1
ampersand_index = url_parameters.find('&', value_index)
if ampersand_index == 1:
    parameter_value = url[value_index:]
else:
    parameter_value = url[value_index:ampersand_index]