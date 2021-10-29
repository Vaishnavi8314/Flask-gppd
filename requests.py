from flask import Flask, request
a = Flask(__name__)


def Task_1(body):
    dict = {}
    u1 = int(body['u1'])
    u2 = int(body['u2'])
    u3 = int(body['u3'])
    p1 = int(body['p1'])
    p2 = int(body['p2'])
    F = int(body['F'])
    S = u1+u2+u3+p1+p2
    SFR = int(S)/int(F)
    dict['u1'] = u1
    dict['u2'] = u2
    dict['u3'] = u3
    dict['p1'] = p1
    dict['p2'] = p2
    dict['F'] = F
    dict['S'] = S
    dict['SFR'] = SFR
    if SFR <= 15:
        Score = 20
    elif SFR <= 17:
        Score = 18
    elif SFR <= 19:
        Score = 16
    elif SFR <= 21:
        Score = 14
    elif SFR <= 23:
        Score = 12
    elif SFR <= 25:
        Score = 10
    else:
        Score = 0
    dict['Score'] = Score
    return dict


def Task_2(body):
    new_dict = {}
    N = int(body['N'])
    a_F1 = int(body['a_F1'])
    a_F2 = int(body['a_F2'])
    a_F3 = int(body['a_F3'])
    r_F1 = (1/9)*((1/15)*N)
    r_F1 = round(r_F1)
    r_F2 = (2/9)*((1/15)*N)
    r_F2 = round(r_F2)
    r_F3 = (6/9)*((1/15)*N)
    r_F3 = round(r_F3)
    new_dict['a_F1'] = a_F1
    new_dict['a_F2'] = a_F2
    new_dict['a_F3'] = a_F3
    new_dict['r_F1'] = r_F1
    new_dict['r_F2'] = r_F2
    new_dict['r_F3'] = r_F3

    if a_F1 == a_F2 == 0:
        Cadre_Ratio_Marks = 0
    else:
        Cadre_Ratio_Marks = ((a_F1/r_F1) + ((
            a_F2 * 0.6)/r_F2) + (a_F3 * 0.4)/(r_F3) * 12.5)
        if Cadre_Ratio_Marks > 25:
            Cadre_Ratio_Marks = 25
    new_dict['Cadre_Ratio_Marks'] = Cadre_Ratio_Marks
    return new_dict


@a.route('/1', methods=['POST'])
def task():
    body = request.get_json()
    x = Task_1(body)
    return x


@a.route('/2', methods=['POST'])
def TASK():
    body = request.get_json()
    y = Task_2(body)
    return y


if __name__ == '__main__':
    a.run(debug=True)
