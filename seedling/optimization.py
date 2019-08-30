class Optimization:

    def __init__(self):
        return None

    def genetic_algorithm(self, aa_sequence: str, minimize: bool, pool_size: int, func: function) -> str:
        """Generate a Genetic Algorithm to return the top optimized amino acid sequence
        
        Arguments:
            aa_sequence {str} -- Amino Acid Sequence for a Protein
            minimize {bool} -- To Minimize - TRUE, to maximize - FALSE
            pool_size {int} -- How big the gene pool is
            func {function} -- Function to evaluate all amino acid sequences
        
        Returns:
            str -- The Amino Acid sequence of the optimized sequence
        """
        return 