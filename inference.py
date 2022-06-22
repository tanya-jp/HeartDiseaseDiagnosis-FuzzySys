class FuzzyInference:
    def __int__(self):
        pass

    def inference(self, age, bp, bs, cholesterol, hr, ecg, op, cp, exercise, thallium, sex):
        output_sick1, output_sick2, output_sick3, output_sick4, output_healthy = ([] for i in range(5))

        # rules
        # 1
        output_sick4.append(min(age['very_old'], cp(['atypical_anginal'])))
        # 2
        output_sick4.append(min(hr['high'], age(['old'])))
        # 3
        output_sick3.append(min(sex['male'], hr(['medium'])))
        # 4
        output_sick2.append(min(sex['female'], hr(['medium'])))
        # 5
        output_sick3.append(min(cp['non_anginal_pain'], bp(['high'])))
        # 6
        output_sick2.append(min(cp['typical_anginal'], hr(['medium'])))
        # 7
        output_sick3.append(min(bs['true'], age(['mid'])))
        # 8
        output_sick2.append(min(bs['false'], bp(['very_high'])))
        # 9
        output_sick1.append(max(cp['asymptomatic'], age(['very_old'])))
        # 10
        output_sick1.append(max(bp['high'], age(['very_old'])))

        # Chest Pain
        # 11
        output_healthy.append(cp['typical_anginal'])
        # 12
        output_sick1.append(cp['atypical_anginal'])
        # 13
        output_sick2.append(cp['non_anginal_pain'])
        # 14
        output_sick3.append(cp['asymptomatic'])
        # 15
        output_sick4.append(cp['asymptomatic'])

        # Sex
        # 16
        output_sick1.append(sex['female'])
        # 17
        output_sick2.append(sex['male'])

        # Blood Pressure
        # 18
        output_healthy.append(bp['low'])
        # 19
        output_sick1.append(bp['medium'])
        # 20
        output_sick2.append(bp['high'])
        # 21
        output_sick3.append(bp['high'])
        # 22
        output_sick4.append(bp['very_high'])

        # Cholesterol
        # 23
        output_healthy.append(cholesterol['low'])
        # 24
        output_sick1.append(cholesterol['medium'])
        # 25
        output_sick2.append(cholesterol['high'])
        # 26
        output_sick3.append(cholesterol['high'])
        # 27
        output_sick4.append(cholesterol['very_high'])

        # Blood sugar
        # 28
        output_sick2.append(bs['true'])

        # ECG
        # 29
        output_healthy.append(ecg['normal'])
        # 30
        output_sick1.append(ecg['normal'])
        # 31
        output_sick2.append(ecg['abnormal'])
        # 32
        output_sick3.append(ecg['hypertrophy'])
        # 33
        output_sick4.append(ecg['hypertrophy'])

        # Heart Rate
        # 34
        output_healthy.append(hr['low'])
        # 35
        output_sick1.append(hr['medium'])
        # 36
        output_sick2.append(hr['medium'])
        # 37
        output_sick3.append(hr['high'])
        # 38
        output_sick4.append(hr['high'])

        # exercise
        # 39 ----- EX
        output_sick2.append(exercise['true'])

        # Old Peak
        # 40
        output_healthy.append(op['low'])
        # 41
        output_sick1.append(op['low'])
        # 42
        output_sick2.append(op['terrible'])
        # 43
        output_sick3.append(op['terrible'])
        # 44
        output_sick4.append(op['risk'])

        # Thallium
        # 45
        output_healthy.append(thallium['normal'])
        # 46
        output_sick1.append(thallium['normal'])
        # 47
        output_sick2.append(thallium['medium'])
        # 48
        output_sick3.append(thallium['high'])
        # 49
        output_sick4.append(thallium['high'])

        # Age
        # 50
        output_healthy.append(age['young'])
        # 51
        output_sick1.append(age['mild'])
        # 52
        output_sick2.append(age['old'])
        # 53
        output_sick3.append(age['old'])
        # 54
        output_sick4.append(age['very_old'])

