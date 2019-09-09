class School():
    def __init__(self,name=None, roster={}):
        self.name = name
        self.roster = roster
    def add_student(self, fullname, gradelevel):
        if gradelevel in self.roster.keys():
            self.roster[gradelevel].append(fullname)
        else:
            self.roster[gradelevel] = [fullname]
            
    def grade(self, grade):
        if grade in self.roster.keys():
            return self.roster[grade]
        else:
            return [] 
    def sort_roster(self):
        sortedroster = {}
        for grade,fullnames in self.roster.items():
            sortedroster[grade] = sorted(fullnames)
        return sortedroster


