
# run training
# python train_qcnet.py --root D:\datasets\av2 --dataset argoverse_v2 --train_batch_size 1 --val_batch_size 1 --test_batch_size 1 --devices 1 --num_workers 0 --pin_memory False --persistent_workers False --pl2pl_radius 50 --pl2a_radius 30 --a2a_radius 30 --pl2m_radius 50 --a2m_radius 50
# python train_qcnet.py --root D:\datasets\av2 --dataset argoverse_v2 --train_batch_size 1 --val_batch_size 1 --test_batch_size 1 --devices 1 --num_workers 0 --pin_memory False --persistent_workers False --num_historical_steps 50 --num_future_steps 60 --num_recurrent_steps 3 --pl2pl_radius 50 --pl2a_radius 30 --a2a_radius 30 --pl2m_radius 50 --a2m_radius 50

# git 
# git config --global user.name "Yinx03"
# git config --global user.email 15517603575@163.com

# git config --global http.proxy http://proxyUsername:proxyPassword@proxy.server.com:port
# git config --global http.proxy http://127.0.0.1:7897
# git config --global https.proxy http://proxyUsername:proxyPassword@proxy.server.com:port
# git config --global https.proxy http://127.0.0.1:7897