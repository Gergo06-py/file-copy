from os import listdir
from os.path import isfile, join


class FileManager:
    def __init__(self):
        self.__read_file = False

    def read_file(self, filename = None, path = None):
        """ returns: success """

        print("Reading file\nPlease wait...")

        success: bool = False

        if path in [None, ""]:
            
            self.__path = "res"
        else:
            self.__path = path
        
        filename = self.file_manager(filename)

        with open(f"{self.__path}/{filename}", "r", encoding="utf-8") as f:
            self.__data = [line.strip() for line in f]
            self.__read_filename = filename

        success = True
        self.__read_file = True
        
        return success
    
    def write_file(self, filename = None, path = None, data=None):
        """ returns: success """

        success = False

        if self.file_reading_check():
            print("Writing file\nPlease wait...")
            
            if path in [None, ""]:
                
                self.__path = "out"
            else:
                self.__path = path
            
            if filename in [None, ""]:
                
                splitted_filename = self.__read_filename.split(".")
                filename = f"{splitted_filename[0]}_copy.{splitted_filename[1]}"
            
            if data in [None, ""]:
                
                data = self.__data
            
            answer = input(f"Is the filename \"{filename}\" correct? [y/n]\n").lower()

            while answer not in ["", "y", "yes", "n", "no"]:
                answer = input(f"Please answer with yes or no\nIs the filename \"{filename}\" correct? [y/n]\n").lower()

            if answer in ["", "y", "yes"]:
                splitted_filename = self.__read_filename.split(".")
                
                filename_number = 2
                temp_filename = f"{splitted_filename[0]}_copy.{splitted_filename[1]}"

                while temp_filename in [f for f in listdir(f"{self.__path}/") if isfile(join(f"{self.__path}/", f))]:
                    temp_filename = f"{splitted_filename[0]}_copy_{filename_number}.{splitted_filename[1]}"
                    filename_number += 1

                while filename in [f for f in listdir(f"{self.__path}/") if isfile(join(f"{self.__path}/", f))]:
                    new_filename = input(f"A file with that name already exists. Please enter a different filename or press enter to use the default name [{temp_filename}]:\n").removesuffix(f".{splitted_filename[1]}")
                    
                    if new_filename == "":
                        new_filename = temp_filename
                    else:
                        new_filename = f"{new_filename}.{splitted_filename[1]}"
                    
                    filename = new_filename

                with open(f"{self.__path}/{filename}", 'w', encoding="utf-8") as f:
                    for index, item in enumerate(data):
                        if index == len(data) - 1:
                            f.write(item)
                        else:
                            f.write(item + "\n")
                    
                    f.close()
            else:
                return success

            success = True
        return success

    def file_manager(self, filename = None):
        if filename in [None, ""]:
            file_list = [f for f in listdir(f"{self.__path}/") if isfile(join(f"{self.__path}/", f))]
            file_number = 0
            
            if len(file_list) > 1:
                file_number = self.multiple_file_chooser(file_list)
            elif len(file_list) == 0:
                self.__path = "."

                file_list = [f for f in listdir(f"{self.__path}/") if isfile(join(f"{self.__path}/", f))]
                
                try:
                    file_list.pop(file_list.index("main.py"))
                    file_list.pop(file_list.index("file_manager.py"))
                except:
                    pass
                    
                if len(file_list) > 1:
                    file_number = self.multiple_file_chooser(file_list)
                elif len(file_list) == 0:
                    print("No files were found to copy.\nCreating a new test file...")

                    with open(f"{self.__path}/test.txt", "x", encoding="utf-8") as f:
                        f.write("test")
                        f.close()
                    return "test.txt"
                
            return file_list[file_number]
        else:
            if filename in listdir(f"{self.__path}/"):
                return filename
            else:
                self.__path = "."

                try:
                    file_list.pop(file_list.index("main.py"))
                    file_list.pop(file_list.index("file_manager.py"))
                except:
                    pass

                if filename in listdir(f"{self.__path}/"):
                    return filename
                else:
                    print("The specified file was not found.\nCreating a new test file...")

                    with open(f"{self.__path}/test.txt", "x", encoding="utf-8") as f:
                        f.write("test")
                        f.close()
                    return "test.txt"
    
    def multiple_file_chooser(self, file_list):
        print("There are multiple files to read from. Please select one from below by typing their number:\n")

        for index, filename in enumerate(file_list):
            print(f"[{index}] \"{filename}\"")
        
        print("Please enter the number below:")

        file_number = None
        
        while file_number is None or file_number > len(file_list) - 1 or file_number < 0:
            try:
                file_number = int(input())

                if file_number > len(file_list) - 1 or file_number < 0:
                    print("Please type a number between 0 and", len(file_list) - 1)
            except:
                print("Please type a number: ")
        
        return file_number
    
    def copy_file(self, read_filename = None, read_path = None, write_filename = None, write_path = None, write_data = None):
        self.read_file(read_filename, read_path)
        self.write_file(write_filename, write_path, write_data)
        
        print("file copy successful")
    
    def file_reading_check(self):
        """ Returns True if the file was read with the read_file() function """

        if self.__read_file:
            return True
        else:
            print("No file was read. Please run read_file() first.")
            return False
    
    def get_data(self):
        if self.file_reading_check():
            return self.__data
    
    def print_data(self):
        for item in self.get_data():
            print(item)
