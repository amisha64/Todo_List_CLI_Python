import sys

class Task:
    @staticmethod
    def helpp() :
        help="""
Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics
    """
        sys.stdout.buffer.write(help.encode('utf8'))

    @staticmethod
    def add(args) :
        if (len(args) == 0) :
            print("Error: Missing tasks string. Nothing added!")
        myObj =  open("task.txt","a+")
        i = 0
        while (i < len(args)) :
            myObj.write(args[i] + " ")
            i += 1
        myObj.write("\n")
        print("Added task: \"", end ="")
        print(args[1],end="")
        index=args[0]
        print("\" with priority " + str(index), end ="")
        myObj.close()

    @staticmethod
    def ls() :
        with open("task.txt" , "a+") as reader:
            reader.seek(0)
            line = reader.readlines()
            if len(line)>0:
                for i in range(len(line)):
                    output=f"{i+1}. {line[i][2:-1]}[{line[i][0]}]\n"
                    sys.stdout.buffer.write(output.encode('utf8'))
            else:
                done = 'There are no pending tasks!\n'
                sys.stdout.buffer.write(done.encode('utf8'))

    @staticmethod
    def dell(delindex) :
        with open("task.txt", "a+") as reader:
            reader.seek(0)
            line=reader.readlines()
        if delindex>len(line) or delindex<1:
            missing=f"Error: task with index #{delindex} does not exist. Nothing deleted."
            sys.stdout.buffer.write(missing.encode('utf8'))
        else:
            with open("task.txt", "w") as writer:
                for i in range(len(line)):
                    if i+1 != delindex:
                        writer.write(line[i])
            output=f"Deleted task #{delindex}"
            sys.stdout.buffer.write(output.encode('utf8'))

    @staticmethod
    def done(doneindex) :
        with open("task.txt", "a+") as reader:
            reader.seek(0)
            line=reader.readlines()
        if doneindex>len(line) or doneindex<1:
            missing=f"Error: no incomplete item with index #{doneindex} exists."
            sys.stdout.buffer.write(missing.encode('utf8'))
        else:
            d=line.pop(doneindex-1)
            with open("task.txt", "w") as file:
                for i in line:
                        file.write(i)
            with open("completed.txt", "a") as file:
                file.write(d[2:])
            output='Marked item as done.'
            sys.stdout.buffer.write(output.encode('utf8'))

    @staticmethod
    def report() :
        with open("task.txt", "a+") as file:
            file.seek(0)
            line=file.readlines()
        output=f"Pending : {len(line)}\n"
        sys.stdout.buffer.write(output.encode('utf8'))
        if len(line)>0:
            for i in range(len(line)):
                output=f"{i+1}. {line[i][2:-1]}[{line[i][0]}]"
                sys.stdout.buffer.write(output.encode('utf8'))
        with open("completed.txt", "a+") as file:
            file.seek(0)
            line2=file.readlines()
        output=f"\n\nCompleted : {len(line2)}\n"
        sys.stdout.buffer.write(output.encode('utf8'))
        if len(line2)>0:
            for i in range(len(line2)):
                output=f"{i+1}. {line2[i][:-2]}\n"
                sys.stdout.buffer.write(output.encode('utf8'))


if __name__=="__main__":
    def main(*args) :
        if (len(sys.argv) == 1 or sys.argv[1]=="help") :
            Task.helpp()
        if (len(sys.argv) != 1 and sys.argv[1]=="add") or (len(args)!=0 and args[1]=="add"):
            try :
                Task.add(sys.argv[2:])
            except Exception as e :
                print(e)
                print("Some error occured", end ="")
        if (len(sys.argv) != 1 and sys.argv[1]=="ls") :
            Task.ls()
        if (len(sys.argv) != 1 and sys.argv[1]=="del") :
            if (len(sys.argv) >= 2) : 
                try :
                    Task.dell(int(sys.argv[2]))
                except Exception as e :
                    print("Error: Missing NUMBER for deleting tasks.", end ="")
            else :
                print("Error: Missing NUMBER for deleting tasks.", end ="")
        if (len(sys.argv) != 1 and sys.argv[1]=="done") :
            try :
                Task.done(int(sys.argv[2]))
            except Exception as e :
                print("Error: Missing NUMBER for marking tasks as done.", end ="")
        if (len(sys.argv) != 1 and sys.argv[1]=="report") :
            Task.report()

    main()