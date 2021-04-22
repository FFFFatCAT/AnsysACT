# -*- coding:utf-8 -*-
# Project: HiFive
# User:CNLOWAN2
# Author: Louis-PeideWang
# CreateDate: 2021/4/22 19:48

clr.AddReference("Ans.UI.Toolkit")
clr.AddReference("Ans.UI.Toolkit.Base")
from Ansys.UI.Toolkit import *


def init(context):
    ExtAPI.Log.WriteMessage("Init ACT HiFive...")


def ShowMessageBox(analysis_obj):
    MessageBox.Show("Hi five! My first ACT extension is a success!")
