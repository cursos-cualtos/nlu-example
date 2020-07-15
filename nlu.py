from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

def do_analize():
    authenticator = IAMAuthenticator('R_EQw6zHdAy85bzkCkCBo0HZmIQPNIfsBTNh4y1I3GUI')
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2019-07-12',
        authenticator=authenticator
    )

    natural_language_understanding.set_service_url('https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/404bfe28-1acd-459b-9d24-804096ce366d')

    response = natural_language_understanding.analyze(
        text='IBM is an American multinational technology company '
        'headquartered in Armonk, New York, United States, '
        'with operations in over 170 countries.',
        features=Features(
            entities=EntitiesOptions(emotion=True, sentiment=True, limit=2),
            keywords=KeywordsOptions(emotion=True, sentiment=True,
                                    limit=2))).get_result()

    print(json.dumps(response, indent=2))
    return json.dumps(response)