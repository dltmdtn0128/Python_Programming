import pandas as pd

df1 = pd.read_csv('C:\\Users\\Seung Soo\\Desktop\\Python\\Ch10\\파이썬프로그래밍01반_CSV - 복사본.csv', encoding='utf-8',
                  header=0)
i_name = [na for na in df1['이름']]
i_number = [no for no in df1['학번(ID)']]
i_dept = [de for de in df1['소속명']]
i_math = [ma for ma in df1['Math']]
i_eng = [en for en in df1['English']]
i_kor = [ko for ko in df1['Korean']]
im_rank = [mr for mr in df1['Math'].rank(ascending=False)]
ie_rank = [er for er in df1['English'].rank(ascending=False)]
ik_rank = [kr for kr in df1['Korean'].rank(ascending=False)]


class Student:

    def __init__(self, name, number, dept, math, eng, kor, m_rank, e_rank, k_rank):
        self.name = name
        self.number = number
        self.dept = dept
        self.math = math
        self.eng = eng
        self.kor = kor
        self.m_rank = m_rank
        self.e_rank = e_rank
        self.k_rank = k_rank

    def show_info(self):
        info = [[n, no, de] for n, no, de in zip(self.name, self.number, self.dept)]
        return info

    def calc_sum(self):
        sum = [a + b + c for a, b, c in zip(self.math, self.eng, self.kor)]
        return sum

    def calc_aver(self):
        avg = [((a + b + c) / 3) for a, b, c in zip(self.math, self.eng, self.kor)]
        return avg

    def calc_grade(self, n):
        rank = []
        if n == '수학':
            for a in self.m_rank:
                if (a / 41) < 0.3:
                    rank.append('A')

                elif 0.7 > (a / 41) > 0.3:
                    rank.append('B')

                else:
                    rank.append('C')
            return rank
        elif n == '영어':
            for a in self.e_rank:
                if (a / 41) < 0.3:
                    rank.append('A')

                elif 0.7 > (a / 41) > 0.3:
                    rank.append('B')

                else:
                    rank.append('C')
            return rank
        elif n == '국어':
            for a in self.k_rank:
                if (a / 41) < 0.3:
                    rank.append('A')

                elif 0.7 > (a / 41) > 0.3:
                    rank.append('B')

                else:
                    rank.append('C')
            return rank


student = Student(i_name, i_number, i_dept, i_math, i_eng, i_kor, im_rank, ie_rank, ik_rank)

zip_score = list(zip(student.show_info(), student.calc_sum(), student.calc_aver()))
zip_score.sort(key= lambda x:x[1],reverse= True)
print('No\t이름\t\t  학번\t\t\t  학과\t\t\t  총점\t\t평균')
count = 1
for i, j, k in zip_score:
    print('{}\t{} {} {:>12} {:>12} {:>10}'.format(count, i[0], i[1], i[2], j, round(k, 1)))
    count += 1

zip_grades= list(zip(student.show_info(), student.calc_grade('수학'), student.calc_grade('영어'),student.calc_grade('국어')))
zip_grades.sort()
print('No\t  이름\t 학번\t\t수학\t영어\t국어')
count=1
for i,j, k, e in zip_grades:
    print(count,'\t', i[0], i[1], '\t', j, '\t', k, '\t', e)
    count+=1
