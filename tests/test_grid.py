import unittest
import Grid


def diagonal_generator(n : int):
    return (
        (a, b) 
        for a in range(2*n-1)
        for b in ( range(0,a+1) if a < n else  range(0, 2*n-a -1) )
    )

def matrix2d_generator(m : int, n : int):
    return (
        (i, j) for i in range(m) for j in range(n)
    )


class TestGrid(unittest.TestCase):

    def assertInvertibility(self, f, f_inv, domain, codomain):
            
            # extract generators so we can reuse them.
            domain, codomain = list(domain), list(codomain)

            # check f(f_inv) is the identity on the codomain
            self.assertEqual(
                codomain,
                list( map(lambda x: f(f_inv(x)), codomain) )
            )
            # check f_inv(f) is the identity on the domain
            self.assertEqual(
                domain,
                list( map(lambda x: f_inv(f(x)), domain) )
            )
    
    def test_generators(self):
        
        m = 5
        n = 8

        self.assertEqual(
            len(list(diagonal_generator(n))),
            n**2
        )
        self.assertEqual(
            len(list(matrix2d_generator(m, n))),
            m*n
        )

    def test_correct_mapping(self):

        m = 5
        n = 8
        
        self.assertEqual(
            list(
                map(
                    lambda i : Grid.flat_to_diagonal(n, i),
                    range(n*n) 
                )
            ),
            list(diagonal_generator(n))
        )
        self.assertEqual(
            list(
                map(
                    lambda i : Grid.flat_to_matrix2d(n, i),
                    range(m*n) 
                )
            ),
            list(matrix2d_generator(m, n))
        )

    def test_invertibility(self):

        m = 5
        n = 8

        self.assertInvertibility(
            lambda i : Grid.matrix2d_to_flat(n, *i),
            lambda i : Grid.flat_to_matrix2d(n, i),
            matrix2d_generator(m, n),
            range(m*n)
        )
        self.assertInvertibility(
            lambda i : Grid.matrix2d_to_diagonal(n, *i),
            lambda i : Grid.diagonal_to_matrix2d(n, *i),
            matrix2d_generator(m, n),
            diagonal_generator(n)
        )
        self.assertInvertibility(
            lambda i : Grid.flat_to_diagonal(n, i),
            lambda i : Grid.diagonal_to_flat(n, *i),
            range(n*n),
            diagonal_generator(n)
        )
        


