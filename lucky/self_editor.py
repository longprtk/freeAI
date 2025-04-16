# lucky/self_editor.py
import os
import shutil

class SelfEditor:
    def copy_to_new_machine(self):
        print("Lucky is copying itself to a new machine...")
        # Giả sử là sao chép mã nguồn sang một thư mục mới (hoặc máy khác qua mạng)
        new_dir = "lucky_copy"
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
            shutil.copytree("lucky", os.path.join(new_dir, "lucky"))
            print("Lucky has copied itself to a new machine!")
        else:
            print("Copy already exists.")
