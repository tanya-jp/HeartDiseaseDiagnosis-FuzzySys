from fuzzification import Fuzzify
from inference import FuzzyInference
from defuzzification import Defuzzify

fuzzification_res = Fuzzify()
inference_res = FuzzyInference()
defuzzification_res = Defuzzify()


class ProvideResult(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProvideResult, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_final_result(input_dict: dict) -> str:
        age, bp, bs, cholesterol, hr, ecg, op, cp, exercise, thallium, sex =\
            fuzzification_res.fuzzification_result(input_dict)

        fuzzy_sickness = \
            inference_res.inference_result(age, bp, bs, cholesterol, hr, ecg, op, cp, exercise, thallium, sex)

        sickness_level = defuzzification_res.defuzzification_result(fuzzy_sickness)

        return sickness_level


