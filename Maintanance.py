class Maintanance():
    
    m_count = 0
    
    def __init__(self):
        Maintanance.m_count += 1
        
    def Start(self):
        print('Процесс (карусель или представление) запускается')
        
    def Stop(self):
        print('Процесс (карусель или представление) и музыкальное сопровождение останавливаются')
    
    def Music(self):
        print('Запускается музыкальное сопровождение')