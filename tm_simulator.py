import sys 

class Machine:
    transitionTable:dict = dict()
    definitionFile:list = list()
    finalStates:set = set()
    startState = ""
    machineType ="Transducer"
    blank=""
 

    def loadData(self):
        self.startState = self.definitionFile[4]
        self.blank = self.definitionFile[5]
        self.finalStates = self.definitionFile[6].split(',')
        for i, line in enumerate(self.definitionFile[7:]):
            values = line.split(",")
            
            self.transitionTable[(values[0],values[1])] = (values[2],values[3],values[4])

    def run(self,input):
        head = 0
        tape = list(input)
        currentState = self.startState

        while(not(currentState in self.finalStates) and currentState != ""):
            input = (currentState,tape[head])
            if(input in self.transitionTable):
                next = self.transitionTable.get(input)
                currentState = next[0]
                tape[head] = next[1]
                if(next[2] == "L"):
                    if(head == 0):
                       
                        tape = [self.blank] + tape
                    else:
                        head -= 1
                else:
                    if(head == len(tape)-1):
                        tape.append(self.blank)
                    else:
                        head += 1
            else:
                currentState =""

        if(self.machineType =="Transducer"):
           for i, out in enumerate(tape[head:]):
               if(out == self.blank):
                   break
               print(out,end=" ")

        else:
            print(currentState in self.finalStates)
           
               


                
            




if(len(sys.argv) !=3):
    print("Incorrect number of arguments")
    exit()

m = Machine()

try:
    file = open(sys.argv[1])
    input = file.readlines()
    lines = list()
    for line in input:
        line = line.replace('\n','').replace(" ", "").replace("(","").replace(")","")
        lines.append(line)

    m.definitionFile = lines
        
        
except:
    print("cannot open" + sys.argv[1])
    exit()

try:
    file = open(sys.argv[2])
    input = file.readlines()
    lines = list()
    for line in input:
        line = line.replace('\n','').replace(" ", "").replace("(","").replace(")","")
        lines.append(line)
    m.machineType = lines[0]
except:
    print("")

m.loadData()
for i, input in enumerate(lines[1:]):
    m.run(input)
    print("")






    