import numpy as np
import itertools 

class som:
    def __init__(self,h,w,dim_feat):
        self.shape = (h,w,dim_feat)
        self.som = np.zeros((h,w,dim_feat))

        self.sigma0 = 0.0
        self.L0 = 0.0
        self.lam = 0.0

    def init(self,rand_f=np.random.rand):
        self.som = rand_f(*self.shape)

    def sigma(self,t):
        return self.sigma0*np.exp(-t/self.lam)

    def theta(self,dist,radius):
        return np.exp(-(dist**2)/(2*radius**2))

    def L(self,t):
        return self.L0*np.exp(-t/self.lam)

    def update_som(self,bmu,t,d):
        y,x = bmu
        bmu_vec = np.array([y,x])
        for y in range(self.shape[0]):
            for x in range(self.shape[1]):
                curr_vec = np.array([y,x])
                dist = np.linalg.norm((bmu_vec-curr_vec))
                curr_radius = self.sigma(t)
                neigh_penalty = self.theta(dist,curr_radius)
                lr = self.L(t)
                self.som[y,x] += neigh_penalty*lr*(d-self.som[y,x])
    

    def find_bmu(self,d):
        bmus = self.find_bmus(d)
        return bmus[0][0]

    def find_bmus(self,d):
        bmus = []
        for y in range(self.shape[0]):
            for x in range(self.shape[1]):
                dist = np.linalg.norm((d-self.som[y,x]))
                bmus.append(((y,x),dist))
        bmus.sort(key=lambda x: x[1])
        return bmus

    def train(self,data,sigma0,L0,lam,pp=True,stock_inter=False,rand_f=np.random.rand):
        self.sigma0 = sigma0
        self.L0 = L0
        self.lam = lam
        
        self.init(rand_f)
        
        inter = []
        if stock_inter:
            inter = [self.som.copy()]
            
        for t in itertools.count():
            if self.sigma(t) < 1.0 or (pp and t%50 == 0):
                print("t:",t)
                print("sigma:",self.sigma(t))
                print("lr:",self.L(t))
                if self.sigma(t) < 1.0:
                    return inter

            i_data =  np.random.choice(range(len(data)))
            d = data[i_data]
            bmu = self.find_bmu(d)
            self.update_som(bmu,t,d)
            if stock_inter:
                inter.append(self.som.copy())
