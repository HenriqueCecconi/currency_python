url = 'http://bytebank.com/exchange?inputCurrency=real&outputCurrency=dollar&quantity=100'

question_index = url.find('?')
url_base = url[:question_index]
url_parameters = url[question_index+1:]