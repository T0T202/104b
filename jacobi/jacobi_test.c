/* jacobi_test.c
   test the jacobi routine in NR
   Notice that NR use strange 1-based indexing convention (FORTRAN style) */

#include <stdio.h>
#include "nrutil.h"

void jacobi(float **a, int n, float d[], float **v, int *nrot);

int main() {

  int N  /* dimension of the matrix */
    , num_rot  /* number of Jacobi applied */
    , i, j;  /* temp. variables for counter */
  float ** A, ** eigenvectors, * eigenvalues;
  char format[] = "%9.5f";  /* format of output */

  printf("dimension of the matrix: ");  scanf("%i", &N);

  /* the following statement declare FORTRAN-style matrix and vector for NR */
  A = matrix( 1, N, 1, N);  /* must be a symmetric real matrix */
  eigenvectors = matrix( 1, N, 1, N);  /* eigenvectors as columns */
  eigenvalues = vector( 1, N);

  /* get input of A */
  printf("enter a %i x %i matrix (separated by space):\n", N, N);
  for( i = 1; i <= N; i++)
    for( j = 1; j <= N; j++)
      scanf( "%f", &A[i][j]);
  puts("\neigen problem for matrix A:");
  for( i = 1; i <= N; i++) {
    for( j = 1; j <= N; j++)
      printf(format, A[i][j]);
    printf("\n");  /* next line */
  }

  /* solve the eigen problem with NR jacobi routin (A will be changed) */
  jacobi( A, N, eigenvalues, eigenvectors, &num_rot);

  /* output the result here */
  printf( "\nnumber of Jacobi applied: %i\neigenvalues:\n", num_rot);
  for( i = 1; i <= N; i++)
    printf(format, eigenvalues[i]);
  printf("\n");  /* next line */

  puts( "\neigenvectors:");
  for( i = 1; i <= N; i++) {
    for( j = 1; j <= N; j++)
      printf(format, eigenvectors[i][j]);
    printf("\n");  /* next line */
  } printf("\n");  /* next line */

  /* free memory here (strange NR style :-( )*/
  free_matrix( A, 1, N, 1, N);  free_matrix( eigenvectors, 1, N, 1, N);
  free_vector( eigenvalues, 1, N);

  return 0;
}
