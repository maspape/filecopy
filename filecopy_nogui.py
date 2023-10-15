import os
import shutil

def copy_files_with_suffix_or_prefix(source_folder, destination_folder, suffix=None, prefix=None):
    for root, dirs, files in os.walk(source_folder):
        for filename in files:
            source_path = os.path.join(root, filename)
            
            # 拡張子を含むファイル名を取得
            base_name, file_extension = os.path.splitext(filename)

            # サフィックスとプレフィックスを追加
            if suffix:
                new_filename = f"{base_name}{suffix}{file_extension}"
            elif prefix:
                new_filename = f"{prefix}{base_name}{file_extension}"
            else:
                new_filename = filename

            destination_path = os.path.join(destination_folder, new_filename)

            # ファイルをコピー
            shutil.copy(source_path, destination_path)

if __name__ == "__main__":
    source_folder = "指定したフォルダのパス"  # 検索対象のフォルダ
    destination_folder = "コピー先のフォルダのパス"  # コピー先のフォルダ
    suffix = "_copy"  # サフィックスを指定 (Noneにするとコピー元と同じ名前になる)
    # prefix = "copy_"  # プレフィックスを指定 (Noneにするとコピー元と同じ名前になる)
    
    copy_files_with_suffix_or_prefix(source_folder, destination_folder, suffix)
