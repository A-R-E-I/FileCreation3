import os.path
import sys
from os import path

msg = ["New file name:","Existing file name:"];

def main():
    AskInfo();

def AskInfo():
    checkpoint="askinfo"
    whichoption= str(input("1-Create new file\n"
                           "2-Search for an existing file\n"
                           "3-exit\n"
                           "Select an option by typing 1, 2, or 3: "));
    CheckInfo(whichoption, checkpoint);

def CheckInfo(optionwhich,pointcheck):
    global whichfilename;
    match(pointcheck):
        case "askinfo":
            optwhich = ord(optionwhich);
            if(optwhich < 49 or optwhich > 51):
                print("Incorrect response.")
                AskInfo();
            else:
                match(optionwhich):
                    case "1":
                        whichfilename = str(input(msg[0]));
                    case "2":
                        whichfilename = str(input(msg[1]));
                    case "3":
                        print("Goodbye");
                        sys.exit();

                whichfilename = whichfilename + ".txt";
                FileConnectivity();
        case default:
            print("Houston...we have a problem");
            sys.exit();

def FileConnectivity():
    fileDir = os.path.dirname(os.path.realpath("__file__"));
    fileexist = bool(path.exists(whichfilename));

    if(fileexist == True):
        adminfile = open(whichfilename,"r");
        print("File exist");
        PerformAgain();
    else:
        YesNo = str(input("The file name you entered does not exist. Do you want to create it(Y/N)?"));
        match(YesNo.upper()):
            case "Y":
                adminfile = open(whichfilename,"x");
                print("text file created")
                CollectInfo();
                PerformAgain();
            case "N":
                print("Thank you");
                adminfile.close();
                sys.exit();
            case default:
                print("Enter Y or N");
                FileConnectivity()
        
def PerformAgain():
    ifstart = str(input("Would you like to performanother action, (Y)es or (N)o?")).upper();
    match(ifstart):
        case "Y":
            AskInfo();
        case "N":
            print("Thank you");
            sys.exit();
        case default:
            print("Enter Y or N");
            PerformAgain()

def CollectInfo():
    print("Let's begin by creating a username and password for your file.");
    username = str(input("Username: "));
    password = str(input("Password: "));
    WriteToFile(username,password,whichfilename);

def WriteToFile(name,passwd,thefile):
    adminfile = open(thefile,"w");
    adminfile.write(name + "," + passwd);
    adminfile.close();

if __name__ == "__main__":
    main();
