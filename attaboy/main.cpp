#include <iostream>
#include <random>

using namespace std;

int main(int argc, char *argv[])
{
    int m = 2;
    int n = 2;
    int o = 1;
    double beta = 1;
    double ener = 0;
    double ener2 = 0;
    double absmagn = 0;
    double magn = 0;
    double magn2 = 0;
    int u,v;


    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(0, m-1);
    v = dis(gen);
    // lage mxn-matrise
    double ** A = new double*[n];
    for (int i = 0; i < m; i++) {
        A[i] = new double [m];
        for (int j = 0; j < n; j++) {
            A[i][j] = 1.0;
        }
    }

    for (int k = 0; k < o; k++) {
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                u = dis(gen);
                v = dis(gen);
                A[u][v]*A[u][v]
            }
        }
    }

    /*
for k in range(o):
    for i in range(m):
        for j in range(n):
            N = copy.deepcopy(M)
            N[i,j] = - N[i,j]
            if exp( -beta*(S(N) - S(M)) ) >= rand():
                M[i,j] = N[i,j]
    ener += S(M)
    ener2 += S(M)**2
    magn += sum(M)
    absmagn += abs(sum(M))
    magn2 += sum(M)**2

    */


}
