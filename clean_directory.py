import os
import shutil


def make_name(name, dest_list):
    n, e = os.path.splitext(name)
    for file_name in dest_list:
        dn, de = os.path.splitext(file_name)
        if not n[-1].isnumeric():
            if n == dn:
                n = n + '1'
        if n[-1].isnumeric():
            while True:
                if n in dn:
                    n = n[-1] + str(int(n[-1])+1)
                else:
                    break
    return n+e

src = os.path.join(os.environ["USERPROFILE"], "Downloads") # targets the Downloads folder
documents_folder = os.path.join(os.environ["USERPROFILE"], "Documents") #targets the Documents folder for file transfer


word_dest = os.path.join(documents_folder, "Word Files")  # Target folder inside Documents
excel_dest = os.path.join(documents_folder, "Excel Files")
ppt_dest = os.path.join(documents_folder, "PowerPoint Files")
pdf_dest = os.path.join(documents_folder, "PDF Files")
image_dest = os.path.join(documents_folder, "Image Files")
programs_dest = os.path.join(documents_folder, "Programs Files")
zip_dest = os.path.join(documents_folder, "Zip Folders")
python_dest = os.path.join(documents_folder, "Python Files")
#other_dest = 'C:/Users/mario.centis/Documents/Other Files'

word_files = []
excel_files = []
ppt_files = []
pdf_files = []
image_files = []
programs_files = []
zip_folders = []
python_files = []
#other_files = []

for file in os.listdir(src):
    if file.endswith('.doc') or file.endswith('.docx'):
        word_files.append(file)
    elif file.endswith('.xlsx') or file.endswith('.csv'):
        excel_files.append(file)
    elif file.endswith('.ppt') or file.endswith('.pptx'):
        ppt_files.append(file)
    elif file.endswith('pdf'):
        pdf_files.append(file)
    elif file.endswith('.exe') or file.endswith('.msi'):
        programs_files.append(file)
    elif file.endswith('.zip'):
        zip_folders.append(file)
    elif file.endswith('.py'):
        python_files.append(file)
    elif file.endswith('.png') or file.endswith('jpg') or file.endswith('.jpeg'):
        image_files.append(file)
    else:
        continue

# Checks the Downloads folder for each extension type and then moves them to the desiganted folder within Documents

for files in word_files:
    if not os.path.exists(word_dest):
        os.makedirs(word_dest)
    os.rename(os.path.join(src,files), os.path.join(src, make_name(files, os.listdir(word_dest))))
    shutil.move(os.path.join(src, make_name(files, os.listdir(word_dest))), word_dest)

for files in excel_files:
    if not os.path.exists(excel_dest):
        os.makedirs(excel_dest)
    os.rename(os.path.join(src,files), os.path.join(src, make_name(files, os.listdir(excel_dest))))
    shutil.move(os.path.join(src, make_name(files, os.listdir(excel_dest))), excel_dest)

for files in ppt_files:
    if not os.path.exists(ppt_dest):
        os.makedirs(ppt_dest)
    os.rename(os.path.join(src,files), os.path.join(src, make_name(files, os.listdir(ppt_dest))))
    shutil.move(os.path.join(src, make_name(files, os.listdir(ppt_dest))), ppt_dest)

for files in pdf_files:
    if not os.path.exists(pdf_dest):
        os.makedirs(pdf_dest)
    os.rename(os.path.join(src,files), os.path.join(src, make_name(files, os.listdir(pdf_dest))))
    shutil.move(os.path.join(src, make_name(files, os.listdir(pdf_dest))), pdf_dest)

for files in python_files:
    if not os.path.exists(python_dest):
        os.makedirs(python_dest)
    os.rename(os.path.join(src,files), os.path.join(src, make_name(files, os.listdir(python_dest))))
    shutil.move(os.path.join(src, make_name(files, os.listdir(python_dest))), python_dest)

for files in image_files:
    if not os.path.exists(image_dest):
        os.makedirs(image_dest)
    os.rename(os.path.join(src,files), os.path.join(src, make_name(files, os.listdir(image_dest))))
    shutil.move(os.path.join(src, make_name(files, os.listdir(image_dest))), image_dest)

for files in programs_files:
    if not os.path.exists(programs_dest):
        os.makedirs(programs_dest)
    os.rename(os.path.join(src,files), os.path.join(src, make_name(files, os.listdir(programs_dest))))
    shutil.move(os.path.join(src, make_name(files, os.listdir(programs_dest))), programs_dest)

for files in zip_folders:
    if not os.path.exists(zip_dest):
        os.makedirs(zip_dest)
    os.rename(os.path.join(src,files), os.path.join(src, make_name(files, os.listdir(zip_dest))))
    shutil.move(os.path.join(src, make_name(files, os.listdir(zip_dest))), zip_dest)


   
