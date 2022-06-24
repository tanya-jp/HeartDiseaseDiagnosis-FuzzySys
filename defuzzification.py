from fuzzification import OutPutSick
output_sick = OutPutSick()


class Defuzzify:
    def __int__(self):
        pass

    def difuzzy_caculator(self, data):
        points_num = 300
        step = 10. / points_num
        points_of_sickness = [-0.5 + i * step for i in range(points_num + 1)]

        numerator = 0.
        denominator = 0.

        for point in points_of_sickness:

            sick1 = output_sick.outPut_sick1(point)
            sick1 = data['output_sick1'] if sick1 > data['output_sick1'] else sick1

            sick2 = output_sick.outPut_sick2(point)
            sick2 = data['output_sick2'] if sick2 > data['output_sick2'] else sick2

            sick3 = output_sick.outPut_sick3(point)
            sick3 = data['output_sick3'] if sick3 > data['output_sick3'] else sick3

            sick4 = output_sick.outPut_sick4(point)
            sick4 = data['output_sick4'] if sick4 > data['output_sick4'] else sick4

            healthy = output_sick.healthy(point)
            healthy = data['output_healthy'] if healthy > data['output_healthy'] else healthy

            result = max(sick1, sick2, sick3, sick4, healthy)

            numerator += result * point * step
            denominator += result * step

        return numerator/denominator if denominator != 0 else 0

    def defuzzification_result(self, data):
        x_star = self.difuzzy_caculator(data)
        if x_star < 0.5:
            return 'output_healthy'
        if x_star < 1.5:
            return 'output_sick1'
        if x_star < 2.5:
            return 'output_sick2'
        if x_star < 3.5:
            return 'output_sick3'
        else:
            return 'output_sick4'

