# Hill-climbing
作業2-1<br><br>
使用網路上的 Hill Climbing演算法並加上註解<br>
input置於InputResources的input.txt<br>
Hill Climbing演算法置於Service的Hill Climbing.py<br>
main.py主要處理收斂圖<br><br><br>
Hill Climbing<br>
我對Hill Climbing演算法的想法是一種最簡單的優化算法，如果最新的解優於當前解則更新，反之則否<br>
步驟1:先決定一個迭代次數，隨機產生出一個合法解，然後去評估這組解有多好(initial)<br>
步驟2:其中一種方法是將第1步產生的解，隨機挑選一個位置進行更新，以01問題來說就是01對調(transition)<br>
步驟3:將第2步新產生出的解進行評估(evalution)<br>
步驟4:比較第3步評估過後的解是否優於原來的解，若優於原來的解則更新，若無則維持原來的解(determination)<br>
重複2-4步驟直到一開始決定的迭代次數<br><br>
使用Hill Climbing演算法時會因為步驟2使用不同transition而導致陷入了區域最佳解，所以Simulation annealing，用退火係數來允許較差解的產生，以助於跳脫區域最佳解<br><br><br>
