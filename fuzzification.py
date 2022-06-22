class AgeFuzzification:
    def __init__(self):
        pass

    def age_young(self, x):
        if x <= 29:
            return 1
        if 29 < x < 38:
            return (38-x)/(38-29)
        else:
            return 0

    def age_mid(self, x):
        if 33 < x <= 38:
            return (x-33)/(38-33)
        if 38 < x < 45:
            return (45-x)/(45-38)
        else:
            return 0

    def age_old(self, x):
        if 40 < x <= 48:
            return (x-40)/(48-40)
        if 48 < x < 58:
            return (58-x)/(58-48)
        else:
            return 0

    def age_veryold(self, x):
        if 52 < x < 60:
            return (x-52)/(60-52)
        if 60 <= x:
            return 1
        else:
            return 0

    def calc_fuzzy(self, age):
        return dict(
            age_young=self.age_young(age),
            age_mid=self.age_mid(age),
            age_old=self.age_old(age),
            age_veryold=self.age_veryold(age)
        )


class BloodPressure:
    def __init__(self):
        pass

    def bloodPressure_low(self, x):
        if x <= 111:
            return 1
        if 111 < x < 134:
            return (134-x)/(134-111)
        else:
            return 0

    def bloodPressure_medium(self, x):
        if 127 < x <= 139:
            return (x-127)/(139-127)
        if 139 < x < 153:
            return (153-x)/(153-139)
        else:
            return 0


    def bloodPressure_high(self, x):
        if 142 < x <= 157:
            return (x-142)/(157-142)
        if 157 < x < 172:
            return (172-x)/(172-157)
        else:
            return 0

    def bloodPressure_veryhigh(self, x):
        if 154 < x < 171:
            return (x-154)/(171-154)
        if 171 <= x:
            return 1
        else:
            return 0

    def calc_fuzzy(self, bp):
        return dict(
            bloodPressure_low=self.bloodPressure_low(bp),
            bloodPressure_medium=self.bloodPressure_medium(bp),
            bloodPressure_high=self.bloodPressure_high(bp),
            bloodPressure_veryhigh=self.bloodPressure_veryhigh(bp)
        )


class BoolSugar:
    def __init__(self):
        pass

    def bloodSugar_veryhigh(self, x):
        if x <= 105:
            return 0
        if 105 < x < 120:
            return (x - 105) / (120 - 105)
        else:
            return 1

    def calc_fuzzy(self, bs):
        return dict(
            bloodSugar_veryhigh = self.bloodSugar_veryhigh(bs)
        )


class Cholesterol:
    def __init__(self):
        pass

    def cholesterol_low(self, x):
        if x <= 151:
            return 1
        if 151 < x < 197:
            return (197-x)/(197-151)
        else:
            return 0

    def cholesterol_medium(self, x):
        if 188 < x <= 215:
            return (x-215)/(215-188)
        if 215 < x < 250:
            return (250-x)/(250-215)
        else:
            return 0


    def cholesterol_high(self, x):
        if 217 < x <= 263:
            return (x-217)/(263-217)
        if 307 < x < 263:
            return (307-x)/(307-263)
        else:
            return 0

    def cholesterol_veryhigh(self, x):
        if 281 < x < 347:
            return (x-281)/(347-281)
        if 347 <= x:
            return 1
        else:
            return 0

    def calc_fuzzy(self, ch):
        return dict(
            cholesterol_low=self.cholesterol_low(ch),
            cholesterol_medium=self.cholesterol_medium(ch),
            cholesterol_high=self.cholesterol_high(ch),
            cholesterol_veryhigh=self.cholesterol_veryhigh(ch)
        )


class HeartRate:
    def __init__(self):
        pass

    def heartRate_low(self, x):
        if x <= 100:
            return 1
        if 100 < x < 141:
            return (141-x)/(141-100)
        else:
            return 0

    def heartRate_medium(self, x):
        if 111 < x <= 152:
            return (x-111)/(152-111)
        if 152 < x < 194:
            return (194-x)/(194-152)
        else:
            return 0

    def heartRate_high(self, x):
        if 152 < x < 210:
            return (x-152)/(210-152)
        if 210 <= x:
            return 1
        else:
            return 0

    def calc_fuzzy(self, hr):
        return dict(
            heartRate_low=self.heartRate_low(hr),
            heartRate_medium=self.heartRate_medium(hr),
            cholesheartRate_highterol_high=self.heartRate_high(hr)
        )


class ECG:
    def __init__(self):
        pass

    def normal(self, x):
        if x <= 0:
            return 1
        if 0 < x < 0.4:
            return (0.4-x)/0.4
        else:
            return 0

    def abnormal(self, x):
        if 0.2 < x <= 1:
            return (x-0.2)/(1-0.2)
        if 1 < x < 1.8:
            return (1.8-x)/(1.8-1)
        else:
            return 0

    def hypertrophy(self, x):
        if 1.4 < x < 1.9:
            return (x-1.4)/(1.9-1.4)
        if 1.9 <= x:
            return 1
        else:
            return 0

    def calc_fuzzy(self, ecg):
        return dict(
            ECG_normal=self.normal(ecg),
            ECG_abnormal=self.abnormal(ecg),
            ECG_hypertrophy=self.hypertrophy(ecg)
        )


class OldPeak:
    def __init__(self):
        pass

    def oldPeak_low(self, x):
        if x <= 1:
            return 1
        if 1 < x < 2:
            return (2-x)/(2-1)
        else:
            return 0

    def oldPeak_risk(self, x):
        if 1.5 < x <= 2.8:
            return (x-1.5)/(2.8-1.5)
        if 2.8 < x < 4.2:
            return (4.2-x)/(4.2-2.8)
        else:
            return 0

    def oldPeak_terrible(self, x):
        if 2.5 < x < 4:
            return (x-2.5)/(4-2.5)
        if 4 <= x:
            return 1
        else:
            return 0

    def calc_fuzzy(self, op):
        return dict(
            oldPeak_low=self.oldPeak_low(op),
            oldPeak_risk=self.oldPeak_risk(op),
            oldPeak_terrible=self.oldPeak_terrible(op)
        )


class ChestPain:
    def __int__(self):
        pass

    def typical_angina(self, x):
        if x == 1:
            return 1
        else:
            return 0

    def atypical_angina(self, x):
        if x == 2:
            return 1
        else:
            return 0

    def non_angial_pain(self, x):
        if x == 3:
            return 1
        else:
            return 0

    def asymptomatic(self, x):
        if x == 4:
            return 1
        else:
            return 0

    def calc_fuzzy(self, cp):
        return dict(
            typical_angina=self.typical_angina(cp),
            atypical_angina=self.atypical_angina(cp),
            non_angial_pain=self.non_angial_pain(cp),
            asymptomatic=self.asymptomatic(cp)
        )


class Exercise:
    def __init__(self):
        pass

    def OK(self, x):
        if x == 1:
            return 1
        else:
            return 0

    def notOK(self, x):
        if x == 0:
            return 1
        else:
            return 0

    def calc_fuzzy(self, ex):
        return dict(
            OK=self.OK(ex),
            notOK=self.notOK(ex)
        )


class Thallium:
    def __init__(self):
        pass

    def normal(self, x):
        if x == 3:
            return 1
        else:
            return 0

    def medium(self, x):
        if x == 6:
            return 1
        else:
            return 0

    def high(self, x):
        if x == 7:
            return 1
        else:
            return 0

    def calc_fuzzy(self, th):
        return dict(
            normal=self.normal(th),
            medium=self.medium(th),
            high=self.high(th)
        )



class Sex:
    def __init__(self):
        pass

    def female(self, x):
        if x == 1:
            return 1
        else:
            return 0

    def male(self, x):
        if x == 0:
            return 1
        else:
            return 0

    def calc_fuzzy_sex(self, s):
        return dict(
            male=self.male(s),
            female=self.female(s)
        )


class OutPutSick:
    def __int__(self):
        pass

    def outPut_sick1(self, x):
        if 0 < x <= 1:
            return x
        if 1 < x <= 2:
            return 2 - x
        else:
            return 0

    def outPut_sick2(self, x):
        if 1 < x <= 2:
            return x - 1
        if 2 < x <= 3:
            return 3 - x
        else:
            return 0

    def outPut_sick3(self, x):
        if 2 < x <= 3:
            return x - 2
        if 3 < x <= 4:
            return 4 - x
        else:
            return 0

    def outPut_sick4(self, x):
        if 3 < x <= 3.75:
            return (x-3)/(3.75-3)
        if 3.75 < x:
            return 1
        else:
            return 0

    def healthy(self, x):
        if x <= 0.25:
            return 1
        if 0.25 < x <= 1:
            return (1-x)/(1-0.25)
        else:
            return 0


