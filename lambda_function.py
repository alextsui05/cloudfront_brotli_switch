import os

def lambda_handler(event, context):
  request = event['Records'][0]['cf']['request']
  headers = request['headers']
  if 'accept-encoding' not in headers:
    return request
  _, file_extension = os.path.splitext(request['uri'])
  if file_extension not in ['.js', '.css']:
    return request

  accept_encoding = headers['accept-encoding'][0]['value']
  extension = ''
  if 'br' in accept_encoding:
    extension = '.br'
  elif 'gzip' in accept_encoding:
    extension = '.gz'
  request['uri'] += extension

  return request
