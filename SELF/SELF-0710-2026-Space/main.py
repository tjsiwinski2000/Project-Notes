#TJS - space issue on laptop
# combining windows cmd line tools with disk analysis seemed to work 
#
# cmd line windows clean up tools: 
# cleanmgr /sagerun:1   [run this fefore and after sageset:1]
# cleanmgr /sageset:1
#
# dump file sizes and paths to a text file:
# forfiles /p C:\Users /s /m *.* /c "cmd /c echo @fsize @path" 2>nul > C:\filesizes.txt

def get_top_30():
    """ given: all filesizes || filepaths in text \
        return: top 30 sizes """
    sizes=[]
    with open("c:\\filesizes.txt") as f1:
        for line in f1:
            size = line.split(' ')[0]
            sizes.append(size)
    int_list = [int(x.strip()) for x in sizes if x.strip()]
    top_30 = sorted(int_list, reverse=True)[:30]
    return sizes

def get_top_30_paths(size_list):
    """ return delete commands for top 30 filepaths based on size provided"""
    report =[]
    empty=''
    with open("c:\\filesizes.txt") as f1:
        for line in f1:
            for s in size_list:
                if str(s) in line:
                    # print(line)
                    clean_line = line.replace(str(s),empty)
                    clean_line = clean_line.replace('\\\\', '\\').replace('"',empty)
                    clean_line = "del " + clean_line
                    print(clean_line)
                    report.append(clean_line)
    return report



top_30 = [2885189632, 2220883968, 1589641216, 894246037, 433069712, 325349064, 318943232, 284946496, 272420864, 200809238, 186333144, 186333144, 176781560, 176781560, 174086226, 134819840, 127926272, 116502528, 113953669, 113945029, 100663296, 100600429, 100340679, 99424813, 89695216, 89695216, 89218588, 82428835, 82165760, 79853014]

# print(get_top_30_paths(top_30))
get_top_30_paths(top_30)


