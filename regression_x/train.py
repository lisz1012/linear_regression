#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
reload(sys) 
sys.setdefaultencoding('utf-8') 
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import metrics
def curce_data(x,y,y_pred):
	x=x.tolist()
	y=y.tolist()
	y_pred=y_pred.tolist()
	results=zip(x,y,y_pred)
	results=["{},{},{}".format(s[0][0],s[1][0],s[2][0]) for s in results ]
	return results

def read_data(path):
	with open(path) as f :
		lines=f.readlines()
	lines=[eval(line.strip()) for line in lines]
	X,y=zip(*lines)
	X=np.array(X)
	y=np.array(y)
	return X,y
X_train,y_train=read_data("train_data")
X_test,y_test=read_data("test_data")

#一个对象，它代表的线性回归模型，它的成员变量，就已经有了w，b. 刚生成w和b的时候 是随机的
model = LinearRegression()
#一调用这个函数，就会不停地找合适的w和b 直到误差最小
model.fit(X_train, y_train)
#打印W
print model.coef_
#打印b
print model.intercept_
#模型已经训练完毕,用模型看下在训练集的表现
y_pred_train = model.predict(X_train)
#sklearn 求解训练集的mse
# y_train 在训练集上 真实的y值
# y_pred_train 通过模型预测出来的y值
#计算  (y_train-y_pred_train)^2/n
train_mse=metrics.mean_squared_error(y_train, y_pred_train)
print "训练集MSE:", train_mse

#看下在测试集上的效果
y_pred_test = model.predict(X_test)
test_mse=metrics.mean_squared_error(y_test, y_pred_test)
print "测试集MSE:",test_mse
train_curve=curce_data(X_train,y_train,y_pred_train)
test_curve=curce_data(X_test,y_test,y_pred_test)
print "推广mse差", test_mse-train_mse
'''
with open("train_curve.csv","w") as f :
	f.writelines("\n".join(train_curve))
with open("test_curve.csv","w") as f :
	f.writelines("\n".join(test_curve))
'''


