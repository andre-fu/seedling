from typing import Callable, List
import random
class Optimization:

    # def __init__(self):
    #     return None

    def genetic_algorithm(self, dna_sequence: str, minimize: bool, pool_size: int, fitness: Callable[[str], float]) -> str:
        """Generate a Genetic Algorithm to return the top optimized amino acid sequence
        
        Arguments:
            dna_sequence {str} -- Amino Acid Sequence for a Protein
            minimize {bool} -- To Minimize - TRUE, to maximize - FALSE
            pool_size {int} -- How big the gene pool is
            fitness {Callable[[str], float]} -- Function to evaluate all amino acid sequences
        
        Returns:
            str -- The Amino Acid sequence of the optimized sequence
        """
        
        return 'hellowlrd'
    
    def _mutate(self, parent1: dict, parent2: dict, no_mutate: List[int], fitness: Callable[[str], float]) -> dict:
        """Mutates two 'dna' sequences together
        
        Arguments:
            parent1 {dict} -- {'dna': str, 'fitness': float}
            parent2 {dict} -- {'dna': str, 'fitness': float}
            no_mutate {List[int]} -- List of indicies not to mutate
            fitness {Callable[[str], float]} -- Function to evaluate the fitness of a 'dna' string
        
        Returns:
            dict -- {'dna': mutated sequence (str), 'fitness': numerical evaluation (float)}
        """
        aa = ['A', 'R', 'N', 'D', 'C', 'Q' ,'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
        child_dna = parent1['dna']

        f = True
        while f == True: 
            start: int = random.randint(0, len(parent2['dna'] - 1))
            stop: int = random.randint(0, len(parent2['dna'] - 1))
            if (start) in no_mutate:
                continue
            if (stop) in no_mutate:
                continue 
            else:
                f = False
                break
        
        if (start or stop) in no_mutate:
            return {'error': 'Something is wrong please submit a PR for this code'}
        if start > stop:
            stop, start = start, stop
        child_dna = list(child_dna)
        parent2['dna'] = list(parent2['dna'])
        child_dna[start:stop] = parent2['dna'][start:stop]
        child_dna = ''.join(child_dna)
        parent2['dna'] = ''.join(parent2['dna'])

        f = True 
        while f == True:
            charpos = random.randint(0, len(child_dna) - 1)
            if (charpos in no_mutate):
                continue
            else: 
                f= False
                break
        child_dna = list(child_dna)
        child_dna[charpos] = aa[random.randint(0, len(changes)-1)]
        child_fitness = fitness(child_dna) #remove target 
        child_dna[start:stop] = parent2['dna'][start:stop]
        child_dna = ''.join(child_dna)

        return({'dna': child_dna, 'fitness': child_fitness})

        
