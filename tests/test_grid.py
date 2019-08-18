import unittest
import Grid


class TestGrid(unittest.TestCase):

    def assertInvertibility(self, f, f_inv, domain, codomain):
            
            # extract generators so we can reuse them.
            list_domain, list_codomain = list(domain), list(codomain)

            # check f(f_inv) is the identity on the codomain
            self.assertEqual(
                list_codomain,
                list( map(lambda x: f(f_inv(x)), list_codomain) )
            )
            # check f_inv(f) is the identity on the domain
            self.assertEqual(
                list_domain,
                list( map(lambda x: f_inv(f(x)), list_domain) )
            )
    
    def test_generators(self):
        
        m = 5
        n = 8

        self.assertEqual(
            len(list(Grid.diagonal_generator(n))),
            n**2
        )
        self.assertEqual(
            len(list(Grid.matrix2d_generator(m, n))),
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
            list(Grid.diagonal_generator(n))
        )
        self.assertEqual(
            list(
                map(
                    lambda i : Grid.flat_to_matrix2d(n, i),
                    range(m*n) 
                )
            ),
            list(Grid.matrix2d_generator(m, n))
        )

    def test_invertibility(self):

        m = 5
        n = 8

        self.assertInvertibility(
            lambda i : Grid.matrix2d_to_flat(n, *i),
            lambda i : Grid.flat_to_matrix2d(n, i),
            Grid.matrix2d_generator(m, n),
            range(m*n)
        )
        self.assertInvertibility(
            lambda i : Grid.matrix2d_to_diagonal(n, *i),
            lambda i : Grid.diagonal_to_matrix2d(n, *i),
            Grid.matrix2d_generator(m, n),
            Grid.diagonal_generator(n)
        )
        self.assertInvertibility(
            lambda i : Grid.flat_to_diagonal(n, i),
            lambda i : Grid.diagonal_to_flat(n, *i),
            range(n*n),
            Grid.diagonal_generator(n)
        )
        


