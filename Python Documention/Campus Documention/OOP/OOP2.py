class RangeNilai:
    def __init__(self, nilai):
        self.nilai = nilai
                
    def range(self):
        if self.nilai >= 80 and self.nilai <= 100:
            grade = 'A'
        elif self.nilai >= 71 and self.nilai <= 79:
            grade = 'B+'
        elif self.nilai >= 61 and self.nilai <= 70:
            grade = 'B'
        elif self.nilai >= 50 and self.nilai <= 59:
            grade = 'C'
        else:
            grade = 'D'
            
        return grade
            
def main():
    nilai = int(input('Nilai : '))
    
    nilai1 = RangeNilai(nilai) 
    grade1 = nilai1.range()
        
    print(f'Grade {grade1}')
    
if __name__ == '__main__':
    main()
    