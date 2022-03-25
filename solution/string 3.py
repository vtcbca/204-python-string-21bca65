#create to list student and address which contain name of student and there respected address print student name with its addressfor
#example=
#studnet["om","sai","ram"]
#address=["bardoli","surat","navsari"]

l=[]
count=0
def list(l):
        for i in range(5):
            s=input("enter the student name:")
            l.append(s)
list(l)
def evenlength(l):
    for i in l:
        count=0
        for j in i:
            count=count+1
            if(count%2==0):
                print("the list of {} and its length is {}.".format(l,count))
evenlength(l)



     
