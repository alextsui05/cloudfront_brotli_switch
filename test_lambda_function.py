import unittest

from lambda_function import lambda_handler

class LambdaFunctionTestCase(unittest.TestCase):
  def cloudfront_event(self, accept_encoding, uri):
    return {
      "Records": [
        {
          "cf": {
            "config": {
              "distributionDomainName": "f39zf71drogal6.cloudfront.net",
              "distributionId": "E2AZGABAA0HYOM",
              "eventType": "origin-request",
              "requestId": "bBesc6qP8tNqqsQSLtrrHQccuhGGDhunqcnrtrUx0ppdMqKA-Cy6bg=="
            },
            "request": {
              "clientIp": "2601:646:8500:c610:8995:a83:414b:106e",
              "headers": {
                "x-forwarded-for": [
                  {
                    "key": "X-Forwarded-For",
                    "value": "2601:646:8500:c610:8995:a83:414b:106e"
                  }
                ],
                "user-agent": [
                  {
                    "key": "User-Agent",
                    "value": "Amazon CloudFront"
                  }
                ],
                "via": [
                  {
                    "key": "Via",
                    "value": "1.1 cf87164db1b955269be430fb1ff37d75.cloudfront.net (CloudFront)"
                  }
                ],
                "accept-encoding": [
                  {
                    "key": "Accept-Encoding",
                    "value": accept_encoding
                  }
                ],
                "upgrade-insecure-requests": [
                  {
                    "key": "Upgrade-Insecure-Requests",
                    "value": "1"
                  }
                ],
                "host": [
                  {
                    "key": "Host",
                    "value": "foobar.s3.amazonaws.com"
                  }
                ]
              },
              "method": "GET",
              "origin": {
                "s3": {
                  "authMethod": "origin-access-identity",
                  "customHeaders": {},
                  "domainName": "foobar.s3.amazonaws.com",
                  "path": "",
                  "region": "us-east-1"
                }
              },
              "querystring": "",
              "uri": uri
            }
          }
        }
      ]
    }

  def test_lambda_handler(self):
    self.assertEqual(
      lambda_handler(self.cloudfront_event(accept_encoding='gzip, deflate, br', uri="/packs/application.0332f160.js"), None)['uri'],
      '/packs/application.0332f160.js.br'
    )
    self.assertEqual(
      lambda_handler(self.cloudfront_event(accept_encoding='gzip', uri="/packs/application.0332f160.js"), None)['uri'],
      '/packs/application.0332f160.js.gz'
    )
    self.assertEqual(
      lambda_handler(self.cloudfront_event(accept_encoding='deflate', uri="/packs/application.0332f160.js"), None)['uri'],
      '/packs/application.0332f160.js'
    )
    self.assertEqual(
      lambda_handler(self.cloudfront_event(accept_encoding='gzip, br', uri='/packs/css/foobar.css'), None)['uri'],
      '/packs/css/foobar.css.br'
    )
    self.assertEqual(
      lambda_handler(self.cloudfront_event(accept_encoding='gzip', uri='/packs/css/foobar.css'), None)['uri'],
      '/packs/css/foobar.css.gz'
    )
    self.assertEqual(
      lambda_handler(self.cloudfront_event(accept_encoding='br', uri='/packs/css/foobar.css'), None)['uri'],
      '/packs/css/foobar.css.br'
    )
    self.assertEqual(
      lambda_handler(self.cloudfront_event(accept_encoding='deflate', uri='/packs/css/foobar.css'), None)['uri'],
      '/packs/css/foobar.css'
    )
    self.assertEqual(
      lambda_handler(self.cloudfront_event(accept_encoding='gzip', uri='/packs/media/foobar.svg'), None)['uri'],
      '/packs/media/foobar.svg'
    )
    self.assertEqual(
      lambda_handler(self.cloudfront_event(accept_encoding='br', uri='/packs/media/foobar.svg'), None)['uri'],
      '/packs/media/foobar.svg'
    )
    self.assertEqual(
      lambda_handler(self.cloudfront_event(accept_encoding='deflate', uri='/packs/media/foobar.svg'), None)['uri'],
      '/packs/media/foobar.svg'
    )
