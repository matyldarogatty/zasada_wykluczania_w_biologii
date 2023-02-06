# zasada_wykluczania_w_biologii

Model dwóch populacji, które konkurują o zasoby środowiska przedstawia układ równań:
$\left\{\begin{array}{rcl} 
N_1'(t) = a_1 N_1(t) \left( 1  -  \frac{N_1(t) + \alpha N_2(t)}{K_1}\right) \\
N_2'(t) = a_2 N_2(t) \left( 1 - \frac{N_2(t) + \beta N_1(t)}{K_2}\right) 
\end{array} \right,  $
gdzie 
{\large $N_1$(t), $N_2$(t)}: rozmiary populacji $\mathcal{P}_1$ i $\mathcal{P}_2$ w czasie t.
{\large K}: ograniczona liczba jedzenia i objętość środowiska (maximum populacji, jaka jest w stanie żyć)\\ 
{\large $a$}: współczynnik rozrodczości populacji \\
{\large $\alpha $}: stopień, z jakim druga populacja wpływa na pierwszą \\
{\large $\beta $}: stopień, z jakim pierwsza populacja wpływa na drugą.

#### Symualcje:
##### 1. $a_1=0.8=a_2$:
$\alpha = 1.2, \beta=0.5$ Pomimo, żena początku niebieskia populacja była liczniejsza, przez duży wpływ zielonej populacji na niebieską, niebieska wymarła.
![b1 2na0 5](https://user-images.githubusercontent.com/92950276/217053971-d583b2e8-2139-4526-8eef-c372ab2a19bd.png)


Dla $\alpha,\beta < 1$ występuje symbioza.
![b0na0](https://user-images.githubusercontent.com/92950276/217054041-465f7996-74b8-417f-a83f-dedd33d50d64.png)

##### 2. Dla dużych $a_1$ i $a_2$ można zaobserwować chaos deterministyczny.
![a2na0 7b2na2](https://user-images.githubusercontent.com/92950276/217052238-e5eda271-954a-4867-a008-8241ecc85529.png) ![a0 7na2b2na2chaos](https://user-images.githubusercontent.com/92950276/217052360-1787893f-4b56-4c87-a780-585fa690b244.png)
