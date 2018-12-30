import torch
import torch.nn
import torch.nn.functional as F
from torch.autograd import Variable

import numpy as np
import os
import pickle
class LoggingModule():
	def __init__(self):
		super(LoggingModule, self).__init__()
		class loss_trace_module():
			def __init__(self):
				super(loss_trace_module, self).__init__()
				self.history = []
				self.accumulated_loss = 0
				self.accumulated_data = 0
			def accumulate_loss(self, loss, num_data):
				loss = loss.cpu().data.numpy()
				self.accumulated_loss += loss * int(num_data)
				self.accumulated_data += num_data
				del loss
				del num_data
			def visualize_history(self, save_dir, title):
				sns.set()
				plt.plot(self.history)
				plt.title(title)
				plt.savefig(os.path.join(save_dir,"{}.png".format(title)))
				plt.close()
				return
			def save(self, save_dir):
				x = {
					'history':self.history,
					'accumulated_loss':self.accumulated_loss,
					'accumulated_data':self.accumulated_data,
				}
				pickle.dump(x, open(save_dir,'wb'))
			def load(self, load_dir):
				x = pickle.load(open(load_dir,'rb'))
				self.history = x['history']
				self.accumulated_loss = x['accumulated_loss']
				self.accumulated_data = x['accumulated_data']
			def log(self, loss=False):
				if not loss:
					loss = self.accumulated_loss / self.accumulated_data
					self.history.append(loss)
					self.accumulated_loss = 0 
					self.accumulated_data = 0
					del loss
				else:
					self.history.append(loss)
					del loss
		class performance_trace_module():
			def __init__(self, higher_is_better):
				self.higher_is_better = higher_is_better
				super(performance_trace_module, self).__init__()
				self.history = []
				if higher_is_better:
					self.best = -1000
				else:
					self.best = 1000
				self.num_evaluation = -1
				self.best_idx = -1
			def visualize_history(self, save_dir, title):
				sns.set()
				plt.plot(self.history)
				plt.title(title)
				plt.savefig(os.path.join(save_dir,"{}.png".format(title)))
				plt.close()
				return
			def save(self, save_dir):
				x = {
					'higher_is_better':self.higher_is_better,
					'history':self.history,
					'best':self.best,
					'best_idx':self.best_idx,
					'num_evaluation':self.num_evaluation,
				}
				pickle.dump(x, open(save_dir, 'wb'))
			def load(self, load_dir):
				x = pickle.load(open(load_dir, 'rb'))
				self.history = x['history']
				self.higher_is_better = x['higher_is_better']
				self.best = x['best']
				self.best_idx = x['best_idx']
				self.num_evaluation = x['num_evaluation']
			def log(self, performance):
				self.num_evaluation += 1
				self.history.append(performance)
				if self.higher_is_better:
					if self.best < performance:
						self.best = performance
						self.best_idx = self.num_evaluation
						return True
				else:
					if self.best > performance:
						self.best = performance
						self.best_idx = self.num_evaluation
						return True
				return False
		self.loss_trace_module = loss_trace_module
		self.performance_trace_module = performance_trace_module
