  
class Memento:
    def __init__(self, file, content):
          
        self.file = file
        self.content = content
  
  
class FileWriterUtility:
  
    def __init__(self, file):
  
        """store the input file data"""
        self.file = file
        self.content = ""
  
    """Write the data into the file"""
  
    def write(self, string):
        self.content += string
  
    """save the data into the Memento"""
  
    def save(self):
        return Memento(self.file, self.content)
  
    """UNDO feature provided"""
  
    def undo(self, memento):
        self.file = memento.file
        self.content = memento.content
  
"""CareTaker for FileWriter"""
  
class FileWriterCaretaker:
  
    """saves the data"""
  
    def save(self, writer):
        self.obj = writer.save()
  
    """undo the content"""
  
    def undo(self, writer):
        writer.undo(self.obj)
  
  
if __name__ == '__main__':
  
    """create the caretaker object"""
    caretaker = FileWriterCaretaker()

    car_wishList = list()
  
    """create the writer object"""
    writer = FileWriterUtility(car_wishList)
  
    """write data into file using writer object"""
    writer.write("Honda 2019\n")
    print(writer.content + "\n\n")
  
    """save the file"""
    caretaker.save(writer)
  
    """again write using the writer """
    writer.write("Toyota 2017\n")
  
    print(writer.content + "\n\n")
  
    """undo the file"""
    caretaker.undo(writer)
  
    print(writer.content + "\n\n")