import os
import shutil
from xml.dom import minidom

config = 'configMac.xml'

# base class for evry file
class TransferFile:

    def __init__(self, src, dst, file_name):

        self.file_name = file_name

        source = os.path.join(src, file_name)

        # checking is it a full path
        if not os.path.exists(source):
            # checking if there are some unnessary charachters in source_path
            if target[0] == "/" or target[0] == '\\':
                target = target[1:]

            running_file = os.getcwd()
            current_directory = os.path.dirname(running_file)
            self.src = os.path.join(current_directory, source)

        else:
            self.src = source

        # checking is it a full path
        if not os.path.exists(dst):
            # checking if there are some unnessary charachters in destination_path
            if dst[0] == "/" or dst[0] == '\\':
                dst = dst[1:]

            running_file = os.getcwd()
            current_directory = os.path.dirname(running_file)
            self.dst = os.path.join(current_directory, self.dst)

        else:
            self.dst = dst
    # function for copying
    def copy(self):
        try:
            shutil.copy2(self.src, self.dst)
            print(f"File {self.file_name} was succefully copied from: \n {self.src} \n to the folder: \n {self.dst} \n")
        except IOError as e:
            print(f"Unable to copy file. \n {e}")
        except:
            print("Unexpected error")


def main():

    mydoc = minidom.parse(config)
    files = mydoc.getElementsByTagName('file')


    for f in files:
        copying = TransferFile(
            f.attributes['source_path'].value,
            f.attributes['destination_path'].value,
            f.attributes['file_name'].value)
        copying.copy()



if __name__ == '__main__':
    main()
