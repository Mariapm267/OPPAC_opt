This is a repository focused on the optimization of a Parallel_plate Avalanche Counter with Optical Readout by using differentiable programming and machine learning techniques.

-- CAUTION! It is a work in progress!

It contains several tools for the reconstruction of the position of the impining particle, implemented techniques to develop a Neural Network trained to predict the reconstructed position from the detector configuration and the beam position and the tools to optimize the detector performance (reconstruction error) leveraging automatic differentiation.

This is a derivative work from: https://github.com/GilesStrong/tomopt, TomOpt: Differential Muon Tomography Optimisation


HOW DOES IT WORK:

 -   From OPPAC_sim simulation files, pre-processing is done with examples/run_preprocessing.py
 -   Once we have a file: preprocessed_datasets.pickle, examples/run_split_data.py will split data into hyperparameter tuning datasets, training datasets and an evaluation dataset.
 -   Then, the hyperparameter tuning  of the NN can be done with examples/run_optuna.py
 -   The NN can be trained and evaluated with examples/run_nn.py, the model is saved as a .pt
 -   Then, the optimization loop can be done using examples/run_opt.py by specifying the model and the number of alphas in the Alpha Batch.
   

References: 

[1] G. C. Strong, M. Lagrange, A. Orio, A. Bordignon, F. Bury, T. Dorigo, A. Gi-
ammanco, M. Heikal, J. Kieseler, M. Lamparth, P. Martínez Ruíz del Árbol, F.
Nardi, P. Vischia, and H. Zaraket, “TomOpt: Differential optimisation for task- and
constraint- aware design of particle detectors in the context of muon tomography”,
ArXiv:2309.14027, 2023.

[2] M. Cortesi, Y. Ayyad, and J. Yurkon, “Development of a parallel-plate avalanche
counter with optical readout (O-PPAC)”, Journal of Instrumentation, vol. 13, no.
10, pp. P10006-P10006, 2018
