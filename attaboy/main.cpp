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
    double T = atof(argv[1]);
    int N = atoi(argv[2]);
    int n = atoi(argv[3]);
    int samples = atoi(argv[4]);
    int thd = 8;

    /*double T = 2.2;
    int N = 10000;
    int n = 20;
    int samples = 10;
    int thd = 1;
*/
    double mini = 1;
    double maxi = log10(N)*log(10);
    double ds = (maxi - mini)/samples;
    int m = n;
    double beta = 1/T;

    # pragma omp parallel num_threads(thd)
    {
            ofstream outfile;
            random_device rd;
            mt19937 gen(rd());
            uniform_int_distribution<int> randnum(0, 100000000);
            outfile.open("file_" + to_string(n) + " " + to_string(T) + " " + to_string(randnum(gen) ) + ".txt");

            int threshold = 1;
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
            for (int k = 1; k <= N; k++) {
                for (int i = 0; i < m; i++) {
                    for (int j = 0; j < n; j++) {
                        int u = rand_m(gen);
                        int v = rand_n(gen);
                        double dE = 2*A[u][v]*(A[u][mod(v+1,n)] + A[mod(u+1, m)][v] +
                                 A[u][mod(v-1 , n)] +  A[mod(u-1 , m)][v]);
                        if (exp(-beta*dE) > randouble(gen) ) {
                            A[u][v] = - A[u][v];
                            E += dE;
                            M += 2*A[u][v];
                        }
                    }
                }
                float tmp = round(( log(k) - mini )/ds);
                if ( tmp > threshold || k == N-1) {
                    outfile << k << ' ' << n << ' ' << T << ' ' << E << ' ' << M << endl;
                    threshold = tmp;
                }
            }
        delete [] A;
        outfile.close();
        }
}
