class File:
    def __init__(self, fileName, fileExtention, content, locked, parentFolder):
        self.fileName = fileName
        acceptableFileExtentions = [".word", ".png", ".js", ".css", ".html", ".mp4", ".mp3", ".pdf"]
        if fileExtention not in acceptableFileExtentions:
            self.fileExtention = ".txt"
        else:
            self.fileExtention = fileExtention
        self.content = content
        self.locked = locked
        self.parentFolder = parentFolder

    def getLifetimeBandwithSize(self):
        counter = 0
        for char in self.content:
            counter += 1
        size = 10 * counter
        return str(size) + "MB"

    def getFileType(self):
        if self.fileExtention == ".pdf" or self.fileExtention == ".word" or self.fileExtention == ".txt":
            return "document"
        elif self.fileExtention == ".js" or self.fileExtention == ".css" or self.fileExtention == ".html":
            return "source-code"
        elif self.fileExtention == ".mp4":
            return "video"
        else:
            return "music"
    
    def prependContent(self, data):
        if self.locked == False:
            self.content = data + self.content
            return self.content
        else:
            return "You cannot edit the file since it is locked."
        
    def appendContent(self, data):
        if self.locked == False:
            self.content += data
            return self.content
        else:
            return "You cannot edit the file since it is locked."

    def addContent(self, data, position):
        if self.locked == False:
            self.content = self.content[:position] + data + self.content[position:]
            return self.content
        else:
            return "You cannot edit the file since it is locked."
    
    def showFileLocation(self):
        return self.parentFolder + " > " + self.fileName + self.fileExtention

# assignment
# .word
# Something that occurs too early before preparations are ready. Starting too soon.
# false
# homework

assignment = File("assignment", ".word", "Something that occurs too early before preparations are ready. Starting too soon.", False, "homework")
print(assignment.getLifetimeBandwithSize())
print(assignment.getFileType())
print(assignment.prependContent("good morning "))
print(assignment.appendContent(" good evening."))
print(assignment.addContent("hello world ", 13))
print(assignment.showFileLocation())