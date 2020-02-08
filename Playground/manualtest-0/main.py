########### Python 3.6 #############
import requests

LUIS_OFF = False


def texttoluis(query) -> str:
    if LUIS_OFF:
        return dummy_response_if_a_is_less_than_b
    # TODO: change dummy response to Response type instead of dictionary
    # <class 'requests.models.Response'>
    # < Response[200] >
    # {'query': .... }

    try:
        key = '9684c3a770044492ad371464052f5929'  # your Runtime key
        endpoint = 'westus.api.cognitive.microsoft.com/'
        appId = '843c10a1-2b5a-4f22-acf1-c4c09cbce6b3'
        utterance = query

        headers = {
        }

        params = {
            'query': utterance,
            'timezoneOffset': '0',
            'verbose': 'true',
            'show-all-intents': 'true',
            'spellCheck': 'false',
            'staging': 'false',
            'subscription-key': key
        }

        r = requests.get(f'https://{endpoint}/luis/prediction/v3.0/apps/{appId}/slots/production/predict',
                         headers=headers,
                         params=params)
        return r

    except Exception as e:
        print(f'{e}')


if __name__ == '__main__':
    res = texttoluis('if a is less than b')
    print(type(res))
    print(res)
    print(res.json())

dummy_response_if_a_is_less_than_b = {
    "query": "if a is less than b",
    "prediction": {
        "topIntent": "if",
        "intents": {
            "if": {"score": 0.9957939},
            "def function": {"score": 0.00298111956},
            "class": {"score": 0.00291170366},
            "None": {"score": 0.00189279171},
            "var_assignment": {"score": 0.00119137589}
        },
        "entities": {
            "operation": [
                {
                    "operand_1": ["a"],
                    "operator": ["less than"],
                    "operand_2": ["b"],
                    "$instance": {
                        "operand_1": [
                            {
                                "type": "operand_1",
                                "text": "a",
                                "startIndex": 3,
                                "length": 1,
                                "score": 0.9946836,
                                "modelTypeId": 1,
                                "modelType": "Entity Extractor",
                                "recognitionSources": ["model"]
                            }
                        ],
                        "operator": [
                            {
                                "type": "operator",
                                "text": "less than",
                                "startIndex": 8,
                                "length": 9,
                                "score": 0.9672605,
                                "modelTypeId": 1,
                                "modelType": "Entity Extractor",
                                "recognitionSources": ["model"]
                            }
                        ],
                        "operand_2": [
                            {
                                "type": "operand_2",
                                "text": "b",
                                "startIndex": 18,
                                "length": 1,
                                "score": 0.9917454,
                                "modelTypeId": 1,
                                "modelType": "Entity Extractor",
                                "recognitionSources": ["model"]
                            }
                        ]
                    }
                }
            ],
            "keyword": [["if"]],
            "$instance": {
                "operation": [
                    {
                        "type": "operation",
                        "text": "a is less than b",
                        "startIndex": 3,
                        "length": 16,
                        "score": 0.9802576,
                        "modelTypeId": 1,
                        "modelType": "Entity Extractor",
                        "recognitionSources": ["model"]
                    }
                ],
                "keyword": [
                    {
                        "type": "keyword",
                        "text": "if",
                        "startIndex": 0,
                        "length": 2,
                        "modelTypeId": 5,
                        "modelType": "List Entity Extractor",
                        "recognitionSources": ["model"]
                    }
                ]
            }
        }
    }
}
