
# driver code
wt = [2,3,4,5]
v = [3,4,5,6]
W = 5
n = len(v)

# We initialize the matrix with -1 at first.
T = [[-1 for i in range(W + 1)] for j in range(n + 1)]

for i in range(n+1):
        for j in range(W+1):
            if i==0 or j==0:
                T[i][j]=0

            elif(wt[i-1]<=j):
                if(T[i-1][j]>T[i-1][j-wt[i-1]]+v[i-1]):
                    T[i][j]=T[i-1][j]

                else:
                    T[i][j]=T[i-1][j-wt[i-1]]+v[i-1]    

            else:
                T[i][j] = T[i-1][j]

print(T)