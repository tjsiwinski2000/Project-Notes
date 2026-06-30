#0115-2026 Show current AWS users
import subprocess
def main_function():
    result = subprocess.run("aws iam list-users", capture_output = True, text=True, shell=True)
    # output is 'dirty'
    # remove extra lines , characters etc...
    output = result.stdout.replace("[","").replace("]","").replace("{","").replace("}","").replace("  ","").replace("\n","")
    output_list=output.split(",")
    # print(type(output_list))
    print("=" * 60)
    for item in output_list:
        if item.__contains__("User") or item.__contains__("Create") or item.__contains__("Password") :
            print(item.replace('"',''))
    print("=" * 60)
    
if __name__ == "__main__":
    main_function()
