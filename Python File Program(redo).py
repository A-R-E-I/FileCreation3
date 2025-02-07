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
        case 'askinfo':
            optwhich = ord(str(optionwhich));
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
                        
                CheckFile();
                whichfilename = whichfilename + Extension;        
                FileConnectivity();
        case default:
            print("Houston...we have a problem");
            sys.exit();

def CheckFile():
    global Extension;
    Filetype = str(input("what kind of file do you want (1. doc, 2. text, 3. excel, 4. pdf)"));
    match(Filetype):
        case "1":
            Extension = ".doc";
        case "2":
            Extension = ".txt";
        case "3":
            Extension = ".xlsx";
        case "4":
            Extension = ".pdf";
        case default:
            print("please enter 1, 2, 3, or 4");
            CheckFile();

def FileConnectivity():
    fileDir = os.path.dirname(os.path.realpath("__file__"));
    fileexist = bool(path.exists(whichfilename));

    if(fileexist == True):
        adminfile = open(whichfilename,"r");
        print("File exist");
    else:
        
        adminfile = open(whichfilename,"x");
        print("text file created")

    adminfile.close();

if __name__ == "__main__":
    main();
