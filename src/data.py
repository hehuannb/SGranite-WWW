import pandas as pd
import numpy as np
import random


def mimic():
    infile = '/Users/huanhe/Desktop/tenLib/bin/flexi_granite/mimic.csv'
    data = pd.read_csv(infile)  # year month state
    labels, levels = pd.factorize(data.SUBJECT_ID)
    data.SUBJECT_ID = labels
    samples = random.sample(range(data.SUBJECT_ID.max()), 35000)
    subdata = data[data.SUBJECT_ID.isin(samples)]
    labels2, levels2 = pd.factorize(subdata.ICD9_CODE)
    labels3, levels3 = pd.factorize(subdata.Aggmed)
    labels4, levels4 = pd.factorize(subdata.SUBJECT_ID)
    subdata.Aggmed = labels3
    subdata.ICD9_CODE = labels2
    subdata.SUBJECT_ID = labels4
    Vals = subdata.vals.values
    Vals.shape = (Vals.shape[0], 1)
    Subs = subdata.iloc[:, 0:3].values
    N = Subs[:, 0].max() + 1
    T = Subs[:, 1].max() + 1
    K = Subs[:, 2].max() + 1
    siz = np.array([N, T, K])
    return Subs, Vals, siz


def flu():
    infile = '/Users/huanhe/Desktop/tenLib/bin/flexi_granite/influ.txt'
    data = pd.read_csv(infile, sep=',', header=None, names=['vals', 'year', 'month', 'state'])
    data.year = data.year.astype(int)
    data.month = data.month.astype(int)
    data.state = data.state.astype(int)
    Vals = data.vals.values
    Vals.shape = (Vals.shape[0], 1)
    Subs = data.iloc[:, 1:4].values
    N = Subs[:, 0].max() + 1
    T = Subs[:, 1].max() + 1
    K = Subs[:, 2].max() + 1
    siz = np.array([N, T, K])
    return Subs, Vals, siz