class FuzzyInference:
    def __int__(self):
        pass

    def inference_result(self, age, bp, bs, cholesterol, hr, ecg, op, cp, exercise, thallium, sex):
        output_sick1, output_sick2, output_sick3, output_sick4, output_healthy = ([] for i in range(5))

        # rules
        # 1
        output_sick4.append(min(float(age['very_old']), float(cp['atypical_anginal'])))
        # 2
        output_sick4.append(min(float(hr['high']), float(age['old'])))
        # 3
        output_sick3.append(min(float(sex['male']), float(hr['medium'])))
        # 4
        output_sick2.append(min(float(sex['female']), float(hr['medium'])))
        # 5
        output_sick3.append(min(float(cp['non_anginal_pain']), float(bp['high'])))
        # 6
        output_sick2.append(min(float(cp['typical_anginal']), float(hr['medium'])))
        # 7
        output_sick3.append(min(float(bs['true']), float(age['mid'])))
        # 8
        output_sick2.append(min(float(bs['false']), float(bp['very_high'])))
        # 9
        output_sick1.append(max(float(cp['asymptomatic']), float(age['very_old'])))
        # 10
        output_sick1.append(max(float(bp['high']), float(age['very_old'])))

        # Chest Pain
        # 11
        output_healthy.append(float(cp['typical_anginal']))
        # 12
        output_sick1.append(float(cp['atypical_anginal']))
        # 13
        output_sick2.append(float(cp['non_anginal_pain']))
        # 14
        output_sick3.append(float(cp['asymptomatic']))
        # 15
        output_sick4.append(float(cp['asymptomatic']))

        # Sex
        # 16
        output_sick1.append(float(sex['female']))
        # 17
        output_sick2.append(float(sex['male']))

        # Blood Pressure
        # 18
        output_healthy.append(float(bp['low']))
        # 19
        output_sick1.append(float(bp['medium']))
        # 20
        output_sick2.append(float(bp['high']))
        # 21
        output_sick3.append(float(bp['high']))
        # 22
        output_sick4.append(float(bp['very_high']))

        # Cholesterol
        # 23
        output_healthy.append(float(cholesterol['low']))
        # 24
        output_sick1.append(float(cholesterol['medium']))
        # 25
        output_sick2.append(float(cholesterol['high']))
        # 26
        output_sick3.append(float(cholesterol['high']))
        # 27
        output_sick4.append(float(cholesterol['very_high']))

        # Blood sugar
        # 28
        output_sick2.append(float(bs['true']))

        # ECG
        # 29
        output_healthy.append(float(ecg['normal']))
        # 30
        output_sick1.append(float(ecg['normal']))
        # 31
        output_sick2.append(float(ecg['abnormal']))
        # 32
        output_sick3.append(float(ecg['hypertrophy']))
        # 33
        output_sick4.append(float(ecg['hypertrophy']))

        # Heart Rate
        # 34
        output_healthy.append(float(hr['low']))
        # 35
        output_sick1.append(float(hr['medium']))
        # 36
        output_sick2.append(float(hr['medium']))
        # 37
        output_sick3.append(float(hr['high']))
        # 38
        output_sick4.append(float(hr['high']))

        # exercise
        # 39
        output_sick2.append(float(exercise['true']))

        # Old Peak
        # 40
        output_healthy.append(float(op['low']))
        # 41
        output_sick1.append(float(op['low']))
        # 42
        output_sick2.append(float(op['terrible']))
        # 43
        output_sick3.append(float(op['terrible']))
        # 44
        output_sick4.append(float(op['risk']))

        # Thallium
        # 45
        output_healthy.append(float(thallium['normal']))
        # 46
        output_sick1.append(float(thallium['normal']))
        # 47
        output_sick2.append(float(thallium['medium']))
        # 48
        output_sick3.append(float(thallium['high']))
        # 49
        output_sick4.append(float(thallium['high']))

        # Age
        # 50
        output_healthy.append(float(age['young']))
        # 51
        output_sick1.append(float(age['mid']))
        # 52
        output_sick2.append(float(age['old']))
        # 53
        output_sick3.append(float(age['old']))
        # 54
        output_sick4.append(float(age['very_old']))

        return dict(
            output_sick1=max(output_sick1),
            output_sick2=max(output_sick2),
            output_sick3=max(output_sick3),
            output_sick4=max(output_sick4),
            output_healthy=max(output_healthy)
        )

