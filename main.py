import file_manager as fm


file_manager = fm.FileManager()

def main():
    file_copy()

def file_copy():
    file_manager.copy_file(input("Please enter the file name to read: "), input("Please enter the path to the file to read: "), input("Please enter the name of the file you want to write the data to: "), input("Please enter the path of the file you want to write the data to: "))

if __name__ == '__main__':
    main()