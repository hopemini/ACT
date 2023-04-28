# ACT
Android activity Clustering using Tree structure

## Data processing files
Download [Link](https://drive.google.com/file/d/14qcx8VKT7s2SW9u0zchDRZDFud4iYne3/view?usp=sharing) and extract it.
```
$ tar xzvf data_processing.tar.gz
```

## Tree autoencoder training and vector extraction
Train the data 10 iterations with the tree autoencoder and extract the latent vector.
```
$ cd autoencoder/tree
$ . ./train.sh
```

output (n: 0, ..., 9)
```
 autoencoder/tree/log/
 data/tree_23_n/
 data/tree_34_n/
```

## Conv autoencoder training and vector extraction
Train the data 10 iterations with the conv autoencoder and extract the latent vector.
```
$ cd autoencoder/conv
$ . ./train.sh
```
output (n: 0, ..., 9)
```
 autoencoder/conv/log/
 data/conv_re_23_n/
 data/conv_re_34_n/
```

## Test data extraction and data fusion
Test data is extracted based on pre-categorized ground truth and data fusion is performed with weight.
```
$ cd ../../data
$ . ./fusion.sh
```

output (n: 0, ..., 9, f: add, cat,  m: 1, ..., 9)
```
 /data/rico_23_conv_re_23_n_f_0.m
 /data/rico_23_tree_23_n_f_0.m
 /data/tree_23_n_conv_re_23_n_f_0.m
 /data/rico_34_conv_re_34_n_f_0.m
 /data/rico_34_tree_34_n_f_0.m
 /data/tree_34_n_conv_re_34_n_f_0.m
```

## Clustering
Perform data clustering.
```
$ cd ../clustering
$ . ./clustering.sh
```

output
```
 clustering/result/
```

## Evaluation
The clustering result is evaluated by Purity, Normalized Mutual Information (NMI), and Adjusted Rand index (ARI).
```
$ cd ../evaluation
$ . ./evaluation_tree.sh
```

output
```
 evaluation/csv/
```
