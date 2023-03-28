# hill climbing

import numpy as np
import matplotlib.pyplot as plt

def total_valu_size(packing, value, size, max_size): #看現在的背包有沒有符合規則
  v = 0.0  # value總數
  s = 0.0  # size總數
  n = len(packing)
  for i in range(n):
    if packing[i] == 1:
      v += value[i]
      s += size[i]
  if s > max_size:  #如果超過最大重量限制
    v = 0.0 #價值設0
  return (v, s)

def adjacent(packing, rnd): #隨機換一個物品的狀態
  n = len(packing)
  result = np.copy(packing)
  i = rnd.randint(n) 
  if result[i] == 0:
    result[i] = 1
  elif result[i] == 1:
    result[i] = 0
  return result

def solve(rnd, valus, sizes, max_size, max_iter): #數量，隨機數，價值，重量，最大重量，最大迭代次數
  curr_packing = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]) #初始設成全部0 optimial:1,0,1,0,1,0,1,1,1,0,0,0,0,1,1
  print("Initial guess: ")
  print(curr_packing)
  
  (curr_valu, curr_size) = total_valu_size(curr_packing, valus, sizes, max_size) #計算現在狀態
  iteration = 0
  interval = (int)(max_iter / 10) #50
  
  x=[]
  y=[]
  
  while iteration <= max_iter: # 0<500
    adj_packing = adjacent(curr_packing, rnd)#隨機換一個物品的狀態
    (adj_v, _) = total_valu_size(adj_packing, valus, sizes, max_size) #計算調整後的value
    if adj_v > curr_valu:  # 調整過後的value大於現在的value的話就取代
      curr_packing = adj_packing; curr_valu = adj_v
    if iteration % interval == 0: # 印出此iteration次數的最佳解
      x.append((int)(iteration)) #圖的x軸
      y.append((int)(curr_valu)) #圖的y軸
      print("iter = %6d : curr value = %7.0f " % (iteration, curr_valu))
    iteration += 1
  plt.title("hill climbing")
  plt.xlabel("iteration")
  plt.ylabel("value")
  plt.plot(x,y)
  plt.show()
  print("/////////////////////")
  return curr_packing       

def main():
  value = np.array([135, 139, 149, 150, 156, 163, 173, 184, 192, 201, 210, 214, 221, 229, 240])
  size = np.array([70,  73,  77,  80,  82,  87,  90,  94,  98,  106, 110, 113, 115, 118, 120])
  max_size = 750

  print("\nItem value: ")
  print(value)
  print("\nItem size: ")
  print(size)
  print("\nMax total size = %d " % max_size)

  rnd = np.random.RandomState(4)
  max_iter = 500 #迭代次數
  print("\nSettings: ")
  print("max_iter = %d " % max_iter)
  packing = solve(rnd, value, size, max_size, max_iter)
  (v,s) = total_valu_size(packing, value, size, max_size)
  
  print("Finished solve() ")
  
  print("\nBest packing found: ")
  print(packing)
  (v,s) = total_valu_size(packing, value, size, max_size)
  print("\nTotal value of packing = %0.1f " % v)
  print("Total size  of packing = %0.1f " % s)
  print("\nEnd demo ")

if __name__ == "__main__":
  main()