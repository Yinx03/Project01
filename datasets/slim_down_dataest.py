import os
import random
import shutil
from tqdm import tqdm

train_path = r'D:\datasets\av2\train' 
# 保留比例为 0.25
keep_ratio = 0.25 


def slim_dataset_folders():
    # 1. 获取 train 目录下所有的子文件夹名
    all_folders = [f for f in os.listdir(train_path) if os.path.isdir(os.path.join(train_path, f))]
    total_count = len(all_folders)
    
    if total_count == 0:
        print(f"错误：在路径 {train_path} 下没有找到任何子文件夹！")
        return

    print(f"检测到当前训练集共有 {total_count} 个场景文件夹。")

    # 2. 随机打乱文件夹顺序
    random.seed(42) 
    random.shuffle(all_folders)

    # 3. 计算保留和删除的数量
    keep_count = int(total_count * keep_ratio)
    folders_to_delete = all_folders[keep_count:]
    
    print(f"计划：保留 {keep_count} 个文件夹，删除 {len(folders_to_delete)} 个文件夹。")
    confirm = input("确定要执行删除吗？此操作不可逆！(y/n): ")
    
    if confirm.lower() != 'y':
        print("操作取消。")
        return

    # 4. 执行递归删除
    print("正在执行批量删除，请稍候...")
    for folder_name in tqdm(folders_to_delete):
        folder_full_path = os.path.join(train_path, folder_name)
        try:
            # 使用 shutil.rmtree 递归删除非空文件夹
            shutil.rmtree(folder_full_path)
        except Exception as e:
            print(f"删除文件夹 {folder_name} 失败: {e}")

    print(f"清理完成！现在训练集剩余 {len(os.listdir(train_path))} 个场景文件夹。")

if __name__ == "__main__":
    slim_dataset_folders()