import savetocsv
import homework
import print_parser
import autoscout_uas_parser

# num = "3"
start = "4"
match start:
    case "1":
        homework.savetocsv()
    case "2":
        savetocsv.savetocsv()
    case "3":
        print_parser.savetocsv()
    case "4":
        autoscout_uas_parser.savetocsv()

