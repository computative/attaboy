#include <iostream>
#include <random>
#include <cmath>

using namespace std;

// sum over naboer
int S(double **A, int &m, int &n) {
    int s = 0;
    for (int i = 0; i<m; i++){
        for (int j = 0; j<n; j++) {
            s += A[i][j]*A[i][(j+1) % (n)] + A[i][j]*A[(i+1) % (m)][j];
        }
    }
    return -s;
}

int mod(int x, int m) {
    return (x%m + m)%m;
}

int sum(double **A, int &m, int &n) {
    int s = 0;
    for (int i = 0; i<m; i++){
        for (int j = 0; j<n; j++) {
            s += A[i][j];
        }
    }
    return s;
}


int main(int argc, char *argv[])
{
    int m = 3;
    int n = 3;
    // lage mxn-matrise
    double ** A = new double*[m];
    for (int i = 0; i < m; i++) {
        A[i] = new double [n];
        for (int j = 0; j < n; j++) {
            A[i][j] = 1.0;
        }
    }
    int N = 10000;
    double beta = 1;
    double E = S(A,m,n);
    double M = sum(A,m,n);
    double avg [4] = {0,0,0,0};
    int u,v;
    double dE;
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> rand_m(0, m-1);
    uniform_int_distribution<int> rand_n(0, n-1);
    uniform_real_distribution<double> randouble(0.0,1.0);

    for (int k = 0; k < N; k++) {
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                u = rand_m(gen);
                v = rand_n(gen);
                dE = 2*(A[u][v]*A[u][mod(v+1,n)] + A[u][v]*A[mod(u+1, m)][v] +
                        A[u][v]*A[u][mod(v-1 , n)] + A[u][v]*A[mod(u-1 , m)][v]);
                if (exp(-beta*dE) > randouble(gen) ) {
                    A[u][v] = - A[u][v];
                    E += dE;
                    M += 2*A[u][v];
                }
            }
        }
        avg[0] += E;
        avg[1] += E*E;
        avg[2] += abs(M);
        avg[3] += M*M;
    }
    cout << avg[0]/N << ' ' << avg[2]/N << ' '<< avg[1]/N - pow(avg[0]/N,2) << ' ' << avg[3]/N - pow(avg[2]/N,2)<< endl;
}
