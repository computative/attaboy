#include <iostream>
#include <random>
#include <cmath>

using namespace std;

// sum over naboer
int S(double **M, int &m, int &n) {
    int s = 0;
    for (int i = 0; i<n; i++){
        for (int j = 0; j<m; j++) {
            s += M[i][j]*M[i][(j+1) % (n)] + M[i][j]*M[(i+1) % (m)][j];
        }
    }
    return -s;
}

int sum(double **M, int &m, int &n) {
    int s = 0;
    for (int i = 0; i<n; i++){
        for (int j = 0; j<m; j++) {
            s += M[i][j];
        }
    }
    return s;
}


int main(int argc, char *argv[])
{
    int m = 2;
    int n = 2;
    int N = 100000;
    double beta = 1;
    double ener = 0;
    double ener2 = 0;
    double absmagn = 0;
    double magn2 = 0;
    int u,v;
    double dE;

    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> randint(0, m-1);
    uniform_real_distribution<double> randouble(0.0,1.0);


    // lage mxn-matrise
    double ** M = new double*[m];
    for (int i = 0; i < m; i++) {
        M[i] = new double [n];
        for (int j = 0; j < n; j++) {
            M[i][j] = 1.0;
        }
    }

    for (int k = 0; k < N; k++) {
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                u = randint(gen);
                v = randint(gen);
                dE = 2*(M[u][v]*M[u][(v+1) % n] + M[u][v]*M[(u+1) % m][v] +
                        M[u][v]*M[u][abs((v-1) % n)] + M[u][v]*M[abs((u-1) % m)][v]);
                if (exp(-beta*dE) > randouble(gen) ) {
                    M[u][v] = - M[u][v];
                }
            }
        }
        ener   += S(M,m,n);
        ener2  += pow(S(M,m,n),2);
        magn2  += pow(sum(M,m,n),2);
        absmagn += abs(sum(M,m,n));
    }

    cout << ener/N << endl;
    cout << absmagn/N << endl;
    cout << ener2/N - pow(ener/N,2) << endl;
    cout << magn2/N - pow(absmagn/N,2) << endl;
}
