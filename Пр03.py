   import numpy as np, matplotlib.pyplot as plt
   L=2.5; h=1.0; loads=[(3,2e3,-4e3),(4,0,-4e3)]
   nodes={0:np.array([0.,0.]),1:np.array([L,0.]),2:np.array([2*L,0.]),3:np.array([L/2,h]),4:np.array([3*L/2,h])}
   members=[(0,1),(1,2),(3,4),(0,3),(3,1),(1,4),(4,2)]
   m=len(members); n=10
   A=np.zeros((n,m+3)); F=np.zeros(n)
   for nid,fx,fy in loads: F[2*nid]=fx; F[2*nid+1]=fy
   for nid in nodes:
       ex=2*nid
       for mi,(u,v) in enumerate(members):
           if nid in (u,v):
               vec=nodes[v if nid==u else u]-nodes[nid]
               A[ex,mi]+=vec[0]/np.linalg.norm(vec); A[ex+1,mi]+=vec[1]/np.linalg.norm(vec)
       if nid==0: A[ex,m]=1; A[ex+1,m+1]=1
       if nid==2: A[ex+1,m+2]=1
   x=np.linalg.solve(A,-F); N=x[:3+4]
   print('R0x,R0y,R2y',x[7:])
   print('N кН',N/1000)
   print('cond',np.linalg.cond(A))
   print('Автопроверка пройдена')
