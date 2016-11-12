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

    double dt = atof(argv[1]);
    int N = atoi(argv[2]);
    int n = atoi(argv[3]);

    //double dt = 0.05;
    //int N = 100000;
    //int n = 20;

    int m = n;
    int timesteps = (int) ceil(0.4/dt);
    int samplepoint = 10000;
    double * beta = new double [timesteps];
    for (int i = 0; i < timesteps; i++) {
        beta[i] = 1/(2 + (i+1)*dt);
    }

    # pragma omp parallel
    {
        int id = omp_get_thread_num();
        int threads = omp_get_num_threads();
        for (int l = id; l < timesteps; l=l+threads) {
            random_device rd;
            mt19937 gen(rd());
            uniform_int_distribution<int> rand_m(0, m-1);
            uniform_int_distribution<int> rand_n(0, n-1);
            uniform_int_distribution<int> rand_bool(0, 1);
            uniform_real_distribution<double> randouble(0.0,1.0);

            double ** A = new double*[m];
            for (int i = 0; i < m; i++) {
                A[i] = new double [n];
                for (int j = 0; j < n; j++) {
                    A[i][j] = 2*rand_bool(gen) - 1;
                }
            }

            double E = S(A,m,n);
            double M = sum(A,m,n);
            double avg [4] = {0, 0, 0, 0};
            double time = omp_get_wtime();
            for (int k = 0; k < N; k++) {
                for (int i = 0; i < m; i++) {
                    for (int j = 0; j < n; j++) {
                        int u = rand_m(gen);
                        int v = rand_n(gen);
                        double dE = 2*(A[u][v]*A[u][mod(v+1,n)] + A[u][v]*A[mod(u+1, m)][v] +
                                A[u][v]*A[u][mod(v-1 , n)] + A[u][v]*A[mod(u-1 , m)][v]);
                        if (exp(-beta[l]*dE) > randouble(gen) ) {
                            A[u][v] = - A[u][v];
                            E += dE;
                            M += 2*A[u][v];
                        }
                    }
                }
                if (k >= samplepoint) {
                    avg[0] += E;
                    avg[1] += E*E;
                    avg[2] += abs(M);
                    avg[3] += M*M;
                }
            }
            delete [] A;
            # pragma omp critical
            cout << 1/beta[l] << ' ' << omp_get_wtime() - time << ' ' << avg[0]/(N - samplepoint) << ' ' << avg[2]/(N - samplepoint) << ' '<< (avg[1]/(N - samplepoint) - pow(avg[0]/(N - samplepoint),2))*beta[l]*beta[l] << ' ' << (avg[3]/(N - samplepoint) - pow(avg[2]/(N - samplepoint),2))*beta[l] << ' ' <<  endl;
        }
    }
}
