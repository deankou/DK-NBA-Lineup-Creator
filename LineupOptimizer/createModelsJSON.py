import os
import dataStorage

# This creates the json that runOptimizer() uses when spitting out models
# This does not get run everytime the program is run, only when creating new
# models to spit out

libDir = os.getcwd() +"\\lib"

modelNames = ['A_pydfs_1.00_Exp',
              'A_pydfs_0.90_Exp',
              'A_pydfs_0.80_Exp',
              'A_pydfs_0.70_Exp',
              'A_pydfs_0.60_Exp',
              'A_pydfs_0.50_Exp',
              'A_pydfs_0.40_Exp',
              'A_pydfs_0.30_Exp',
              'A_pydfs_0.20_Exp',
              'A_pydfs_0.10_Exp',
              'A_pydfs_0.05_Exp']

modelExp = [1.00,
            0.90,
            0.80,
            0.70,
            0.60,
            0.50,
            0.40,
            0.30,
            0.20,
            0.10,
            0.05]

modelList = [modelNames,modelExp]

dataStorage.storeModels(modelList, libDir)



    
