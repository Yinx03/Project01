
# run training
# python train_qcnet.py --root D:\datasets\av2 --dataset argoverse_v2 --train_batch_size 1 --val_batch_size 1 --test_batch_size 1 --devices 1 --num_workers 0 --pin_memory False --persistent_workers False --pl2pl_radius 50 --pl2a_radius 30 --a2a_radius 30 --pl2m_radius 50 --a2m_radius 50
# python train_qcnet.py --root D:\datasets\av2 --dataset argoverse_v2 --train_batch_size 1 --val_batch_size 1 --test_batch_size 1 --devices 1 --num_workers 0 --pin_memory False --persistent_workers False --num_historical_steps 50 --num_future_steps 60 --num_recurrent_steps 3 --pl2pl_radius 50 --pl2a_radius 30 --a2a_radius 30 --pl2m_radius 50 --a2m_radius 50
# python train_qcnet.py --root D:\datasets\av2 --dataset argoverse_v2 --train_batch_size 1 --val_batch_size 1 --test_batch_size 1 --devices 1 --num_workers 0 --pin_memory False --persistent_workers False --num_historical_steps 50 --num_future_steps 60 --num_recurrent_steps 3 --pl2pl_radius 50 --pl2a_radius 30 --a2a_radius 30 --pl2m_radius 50 --a2m_radius 50 --train_raw_dir D:\datasets\av2\train --val_raw_dir D:\datasets\av2\val --test_raw_dir D:\datasets\av2\test
# git config
# git config --global user.name "Yinx03"
# git config --global user.email 15517603575@163.com

# git config --global http.proxy http://proxyUsername:proxyPassword@proxy.server.com:port
# git config --global http.proxy http://127.0.0.1:7897
# git config --global https.proxy http://proxyUsername:proxyPassword@proxy.server.com:port
# git config --global https.proxy http://127.0.0.1:7897

# Method 1
# GitHub的Fork功能
# (1) fork建立副本仓库
# (2) git clone https:// github.com/Yinx03/----.git
# (3) git add .
# (4) git commit -m "Description"
# (5) git push origin main
# Method 2
# (1) New repository
# (2) git remove -v
# (3) git remote set-url origin https://github.com/Yinx03/Project01.git
# (4) git push -u origin main

# git remote -v 
# origin https://github.com/Yinx03/----.git(fetch)  //fork/clone后的仓库，可读写，用于提交个人的修改
# origin https://github.com/Yinx03/----.git(push)
# upstream https://github.com/ZikangZhou/QCNet.git(fetch)   //origin project：只读，用于获取更新
# upstream https://github.com/ZikangZhou/QCNet.git(push)

# git remote add upstream https://github.com/ZikangZhou/QCNet.git   // 添加原作者仓库为上游
# git pull upstream main // 获取原作者的更新并合并到本地
# git push origin main // 将更新推送到自己的GitHub仓库