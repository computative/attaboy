#include <iostream>
#include <fstream>
#include <random>
#include <cmath>
#include <cstdio>
#include <omp.h>

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

// euklidisk modulo
int mod(int x, int m) {
    return (x%m + m)%m;
}

// matrisenorm
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
    int N = atoi(argv[1]);
    double beta = atof(argv[2]);
    int A0 = atoi(argv[3]);
    int mode = 1;

    int m = 20;
    int n = 20;

    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> rand_m(0, m-1);
    uniform_int_distribution<int> rand_n(0, n-1);
    uniform_int_distribution<int> rand_bool(0, 1);
    uniform_real_distribution<double> randouble(0.0,1.0);

    int a;
    double ** A = new double*[m];
    for (int i = 0; i < m; i++) {
        A[i] = new double [n];
        for (int j = 0; j < n; j++) {
            a = 1;
            if (A0)
                a = 2*rand_bool(gen) - 1;
            A[i][j] = a;
        }
    }

    double E = S(A,m,n);
    double M = sum(A,m,n);
    double avg [4] = {0,0,0,0};
    double ** data  = new double* [N];
    double time = omp_get_wtime();
    for (int k = 0; k < N; k++) {
        int accepts = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int u = rand_m(gen);
                int v = rand_n(gen);
                double dE = 2*(A[u][v]*A[u][mod(v+1,n)] + A[u][v]*A[mod(u+1, m)][v] +
                        A[u][v]*A[u][mod(v-1 , n)] + A[u][v]*A[mod(u-1 , m)][v]);
                if (exp(-beta*dE) > randouble(gen) ) {
                    A[u][v] = - A[u][v];
                    E += dE;
                    M += 2*A[u][v];
                    accepts++;
                }
            }
        }
        data[k] = new double [3];
        data[k][0] = E;
        data[k][1] = M;
        data[k][2] = accepts;

        avg[0] += E;
        avg[1] += E*E;
        avg[2] += abs(M);
        avg[3] += M*M;
    }
    if (mode) {
        ofstream outfile;
        outfile.open("temp.txt");
        for(int k = 0; k < N; k++)
            outfile << data[k][0] << ' ' << data[k][1] << ' ' << data[k][2] << endl;
        outfile.close();
    }
    delete [] data;
    cout << omp_get_wtime() - time << endl;
}
