class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
                
    def Task(self, t1, t2, t3):
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3

    def NA(self):
        return (self.t1 + self.t2 + self.t3) / 3
    
    def Grade(self):
        if dtMHS.NA() >= 80 and dtMHS.NA() <= 100:
            grade = 'A'
        elif dtMHS.NA() >= 70 and dtMHS.NA() <= 79:
            grade = 'B'
        elif dtMHS.NA() >= 60 and dtMHS.NA() <= 69:
            grade = 'C'
        else:
            grade = 'D'   
        return grade
        
p = []

dataMHS = {'Nama' : ' ',
            'Umur' : ' ',
            'Tugas 1' : ' ',
            'Tugas 2' : ' ',
            'Tugas 3' : ' ',
            'Nilai Akhir' : ' ',
            'Grade' : ' '}

k = int(input('Student : '))

for i in range(k):    
    dataMHS['Nama'] = str(input('Nama : '))
    dataMHS['Umur'] = int(input('Umur : '))
    
    n = dataMHS['Nama']
    u = dataMHS['Umur']
    
    t1 = int(input('Tugas 1 : '))
    t2 = int(input('Tugas 2 : '))
    t3 = int(input('Tugas 3 : '))
    
    dataMHS['Tugas 1'] = t1
    dataMHS['Tugas 2'] = t2
    dataMHS['Tugas 3'] = t3
    
    dtMHS = Student(n, u)
    dtTask = dtMHS.Task(t1, t2, t3)
    dtNA = dtMHS.NA()
    
    dataMHS['Nilai Akhir'] = dtNA
    
    dtGRADE = dtMHS.Grade()
    
    dataMHS['Grade'] = dtGRADE
    
    p.append(dataMHS)
        
print('NO', 'Umur', 'Tugas 1', 'Tugas 2', 'Tugas 3', 'NA', 'Grade', 
      sep = ' | ', end = '\n-----------------------------------------------------\n')
for i in range(len(p)):
    print(i + 1, p[i]['Umur'], p[i]['Tugas 1'], p[i]['Tugas 2'], 
          p[i]['Tugas 3'], p[i]['Nilai Akhir'], p[i]['Grade'], sep = '\t| ', end = '\n')